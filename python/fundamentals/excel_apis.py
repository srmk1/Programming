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

# Save the excel
book.save(r'/Users/srmk/Documents/Srikanth/nse-data/stocks/NSEI.xlsx')
book.close()
