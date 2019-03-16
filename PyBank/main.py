#Devin Stern
#Homework 3
#Data Analytics and Visualization Cohort 3

#Import Dependencies
import os
import numpy as np

#import csv file
import csv


#Set path for file
csvpath = os.path.join('..', 'Pybank', 'budget_data.csv')

#Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #Create a list to hold months, money, and change
    months =[]
    money = []
    change=[]

    # Set where the months and money lists start
    for row in csvreader:
        months.append(row[0])
        money.append(int(row[1]))
    
     #count the number of months and sum the money
    monthscount = len(months)
    net = sum(money)

    #get the difference between each row in money
    change = np.diff(money)

    #get the average of change in money
    avgchange = sum(change)/len(change)

    #find the maximum value in the change list
    #find the corresponding date value 
    maxprofit = max(change)
    index_maxprofit = np.nanargmax(change)
    
    #find the minimum value in the change list
    #find the corresponding date value
    minprofit = min(change)
    index_minprofit = np.nanargmin(change)


#build the output summary
output =(

f"Financial Analysis\n"
f"------------------------\n"
f"Total Months: {monthscount}\n"
f"Total: ${net}\n"
f"Average Change: ${avgchange}\n"
f"Greatest Increast in Profits: {months[25]} ${maxprofit}\n"
f"Greatest Decrease in Profits: {months[44]} ${minprofit}\n"
)
print(output)

with open("pybank.txt", 'w') as txt_file:
    txt_file.write(output)


