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


#print everything out
print("Financial Analysis")

print("-----------------------------------")

print (f"Total Months: {monthscount}")
print (f"Total: ${net}")
print(f"Average Change: ${avgchange}")

#index of maxprofit is 24; index of minprofit is 43. Plug in index
#positions of months for maxprofit and minprofit (+1)
print (f"Greatest Increase in Profits: {months[25]} $({maxprofit})")
print (f"Greatest Decrease in Profits: {months[44]} $({minprofit})")

#Export to text file

