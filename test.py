import pandas as pd


mainDF = pd.read_csv("data\processedData.csv")
nDF=mainDF.loc[mainDF["Region"]=="north"].filter(["Date","Sales"])
print(nDF)