import pandas as pd
df = pd.read_csv('robinhood.csv', usecols =[1,4,36,40], header = None)
df.columns = df.iloc[0]
df = df[1:]
df.drop(df[df['total_notional'] != "GME"].index, inplace = True)
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
print(netProfit)
