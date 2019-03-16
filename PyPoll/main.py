#Import Dependencies
import os
import numpy as np

#import csv file
import csv

#Set path for file
csvpath = os.path.join('..', 'PyPoll', 'electiondata.csv')

#Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #Create a list to hold total votes
    votecount = []
    county = []
    candidate = []


    for row in csvreader:
        voterID.append(int(row[0])
        candidate.append(row[2]))


#Grab the length of the votecount list
print(candidates)

#Print Header
print("Election Results")
print("---------------------------")

print(f"Total Votes: {votetotal}")