#! /usr/bin/env python

# Financial data
import yfinance as yf
# Dates and times
import datetime as dt
# Get data for Microsoft, apple, google
df = yf.download(['MSFT', 'AAPL', 'GOOG'], period='1d', interval='1m')

print(df.columns)
print(df['Close'])
# Get the current date and time
filename = dt.datetime.now()
# Create a string from the current date and time
filename = filename.strftime("%Y%m%d_%H%M%S")
# Prepende data folders, append file extension
filename = 'data/' + filename + '.csv'

print(filename)

# Save the data to a CSV file
df['Close'].to_csv(filename)
