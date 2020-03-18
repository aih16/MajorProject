import yfinance as yf


def stockData():

    # Define the ticker symbol
    tickerSymbol = 'USD'

    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-3-17')

    # Open: the stock price at the beginning of that day/month/year
    # High: the highest price the stock achieved that day/month/year
    # Close: the stock price at the end of that day/month/year
    # Low: the lowest price the stock achieved that day/month/year
    # Volume: How many shares were traded that day/month/year

    print(tickerDf)

    with open("stockList.txt", 'w') as f:
        f.write("%s\n" % tickerDf)
        f.close()
