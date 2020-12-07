import os
import csv
print("Financial Analysis")
print("--------------------------------")
csvpath=os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    rowcount=list(csvreader)
    totalmonths=len(rowcount)-1
    print("Total months: " + str(totalmonths))
with open(csvpath) as csvfile:
    totalamount=0
    for row in csv.reader(csvfile):
        csv_header=next(csvfile)
        totalamount+=sum(int(row[2]))
        print("Total: $" + str(totalamount))
