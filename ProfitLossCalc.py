import pandas as pd
import sys

n=len(sys.argv[1])
a=sys.argv[1][1:n-1]
a=a.split(',')
listOfStocks = [str(i).strip() for i in a]
sharesAndNetProfit = {}

for i in listOfStocks:
    df = pd.read_csv('robinhood.csv', usecols =[1,4,36,40], header = None)
    df.columns = df.iloc[0]
    df = df[1:]
    df.drop(df[df['total_notional'] != i].index, inplace = True)
    netProfit = 0
    avgPrice = 0.00
    totalNumofShares = 0
    for index, row in df[::-1].iterrows():
        if(row['stop_price'] == "buy"):
            howManyBought = int(float(row['cumulative_quantity']))
            buyingPrice = float(row['average_price'])
            avgPrice = (avgPrice * totalNumofShares + buyingPrice * howManyBought)/(totalNumofShares + howManyBought)
            totalNumofShares += howManyBought
        elif(row['stop_price'] == "sell"):
            howManySold = int(float(row['cumulative_quantity']))
            sellingPrice = float(row['average_price'])
            netProfit = (avgPrice - sellingPrice)*howManySold
            totalNumofShares -= howManySold
    if i not in sharesAndNetProfit:
        sharesAndNetProfit[i] = netProfit
print(sharesAndNetProfit)
