#Devin Stern
#Homework 3
#Data Visualization Cohort 3

#import dependencies
import pandas as pd
import numpy as np

#name the CSV file
election_file = "electiondata.csv"

#read the CSV file
election_df = pd.read_csv(election_file)

#Calculate total number of votes
candidatenumbers = election_df["Candidate"].value_counts()
candidatenumbers

#total the number of votes cast by summing the candidate counts
totalvotes = candidatenumbers.sum()
totalvotes

#Calculate the percentage of votes each candidate received
candidate_percentage = election_df["Candidate"].value_counts(normalize=True) * 100
candidate_percentage.round()

#Count the votes per candidate
candidate_count = election_df["Candidate"].value_counts()
candidate_count

#Find the percentage of votes won by each candidate
total_stats= pd.concat([candidate_percentage, candidate_count], axis=1)
total_stats.round()

#Take the columns off the dataframe
clean_stats = total_stats.rename(columns={"Candidate":" "})
clean_stats.round()

#Print
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

print("       " "% Votes", " ","Count Votes")

print(f"{clean_stats.round()}")
print("-------------------------")
print(f"Winner: Kahn!")
      

with open("pypoll.txt", 'w') as txt_file:
    txt_file.write(
        "Election Results\n"
        "------------------------\n"
        f"Total Votes: {totalvotes}\n"
        "------------------------\n"
        f"{clean_stats.round()}\n"
        "------------------------\n"
        "Winner: Kahn!"
    )