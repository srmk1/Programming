import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
import datetime

# Add linechart to the sheet
def addLineChart(sheet):
    chart = sheet.charts.add()
    chart.set_source_data(sheet.range('E2').expand())
    chart.chart_type = 'line'
    chart.name = 'Close'

# Add new sheet to the book
def addSheet(book, sheetName, dataFrame):
    sheet = book.sheets.add()
    sheet.name = sheetName
    # Write a panda data-frame to excel
    sheet['A1'].value = dataFrame
    return sheet

# Save the excel
def saveBook(book):
    book.save(r'/Users/srmk/Documents/Srikanth/nse-data/stocks/NSEI.xlsx')

# Read from the sheet to a dataFrame
def readFromSheet(sheet):
    data = sheet['A1'].expand().options(pd.DataFrame).value
    return data

nifty = yf.Ticker("^NSEI")
day1 = datetime.datetime.strptime("2021-01-01","%Y-%m-%d")
seven_days = datetime.timedelta(days=7)
#Open a new excel Workbook
book = xw.Book()

start_date = day1
end_date = day1 + seven_days

for i in range(1, 2):
    df = nifty.history(start=start_date, end=end_date, interval="1h")
    name = "Week#" + str(i)
    sheet = addSheet(book, name, df)
    start_date = end_date
    end_date = end_date + seven_days
    addLineChart(sheet)

# Read the data back to frame
data = readFromSheet(sheet)
print(data)

book.close()
