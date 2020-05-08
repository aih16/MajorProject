import yfinance as yf
import numpy as np


def stockData():

    # Define the ticker symbol
    tickerSymbol = input("Enter ticket symbol: ")

    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Get the historical prices for this ticker
    print("Please provide time frame for stock")
    tickerDf = tickerData.history(period='1d', start=input("Start date (YYYY-MM-DD):"), end=input("End date (YYYY-MM-DD):"))

    # Open: the stock price at the beginning of that day/month/year
    # High: the highest price the stock achieved that day/month/year
    # Close: the stock price at the end of that day/month/year
    # Low: the lowest price the stock achieved that day/month/year
    # Volume: How many shares were traded that day/month/year

    # print(tickerDf)
    # print(tickerDf.Open, tickerDf.Close)

    with open("stockList.txt", 'w') as f:
        openValue = np.array([tickerDf.Open])
        closeValue = np.array([tickerDf.Close])
        differenceValue = closeValue - openValue
        print(differenceValue)

        f.write("%s\n" % tickerDf)
        f.close()
