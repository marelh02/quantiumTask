import csv
import os.path

#the function that writes the processed data in the new csv file
def writeSalesData(writingFile,dataFile):
    flag=os.path.exists('data\\'+writingFile)
    with open('data\\'+writingFile, 'a', newline="") as wFile:
        writerObj=csv.writer(wFile)
        if not(flag):
            writerObj.writerow(["Sales","Date","Region"])
        with open('data\\'+dataFile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
              if row[0]=='pink morsel':
                  writerObj.writerow([float(row[1][1:])*int(row[2]),row[3],row[4]])


#the actual code starts here
dataFile="daily_sales_data_"

for i in range(3):
    writeSalesData("processedData.csv",dataFile+str(i)+".csv")
