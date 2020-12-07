import os
import csv
pybankcsv=os.path.join("Resources", "budget_data.csv")
print("Financial Analysis")
print("--------------------------------")
with open(pybankcsv) as csvfile
    csvreader=csv.reader(csvfile, delimiter=",")
    

