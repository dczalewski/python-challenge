import os
import csv
totalyears=-1
pybankcsv=os.path.join("Resources", "budget_data.csv")
print("Financial Analysis")
print("--------------------------------")
with open(pybankcsv) as csvfile
    csvreader=csv.reader(csvfile, delimiter=",")
    totalyears=totalyears+len(list(budget_data))
    print("Total months: " + totalyears)

