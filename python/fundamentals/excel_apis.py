import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw


# References
# https://www.dataquest.io/blog/python-excel-xlwings-tutorial/

power = yf.Ticker("^NSEI")
df = power.history(start="2020-01-01", end='2020-09-04')
df[['Close']].plot(figsize=(12,12))
# plt.show()

#Open a new excel Workbook
book = xw.Book()

#Access the first sheet
sheet = book.sheets[0]
#rename the name of the sheet
sheet.name = 'Week#1'

# Write a panda data-frame to excel
sheet['A1'].value = df

# Read 52 week OCHL and write it to excel
day1 = datetime.datetime.strptime("2021-01-01","%Y-%m-%d")
seven_days = datetime.timedelta(days=7)
start_date = day1
end_date = day1 + seven_days
for i in range(1, 52):
    df = nifty.history(start=start_date, end=end_date, interval="1h")
    name = "Week#" + str(i)
    sheet = book.sheets.add()
    sheet.name = name
    # Write a panda data-frame to excel
    sheet['A1'].value = df
    start_date = end_date
    end_date = end_date + seven_days

# Read the data back to frame
data = sheet['A1'].expand().options(pd.DataFrame).value

# Save the excel
book.save(r'/Users/srmk/Documents/Srikanth/nse-data/stocks/NSEI.xlsx')
book.close()
