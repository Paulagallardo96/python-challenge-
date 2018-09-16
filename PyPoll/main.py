#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:47:34 2018

@author: paulaamandagallardo
"""

import os
import csv

mypath = "/Users/paulaamandagallardo/Desktop/GWARL201808DATA3-master 2/03-Python/Homework/Instructions/PyPoll/Resources"
csvpath = os.path.join(mypath, 'election_data.csv')

ListOfCandidates = []
CandidateTotal = []
count = 0

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
   
    
    for row in csvreader:
        count = count + 1
        ListOfCandidates.append(row[2])
    
    csvfile.close
    
SetofCandidates =  set(ListOfCandidates)

for candidate in SetofCandidates:
    Votecount = ListOfCandidates.count(candidate)
    candidateTuple = candidate, Votecount, Votecount/count*100
    CandidateTotal.append(candidateTuple)
    
    
winner = max(CandidateTotal,key=lambda item:item[1])[0]


print("Total votes: " + str(count))
print("Winner: " + str(winner))
print("---------------------------------------")

for Tuple in CandidateTotal: 
    print(Tuple[0] + ": " + str( "{:2.2f}".format(Tuple[2]))  + "% (" + str(Tuple[1]) + ")")
    
        
#open text file 
    
with open("PayPoll.txt", "w") as txtfile:
     txtfile.write("Winner: " + str(winner) + "\n")
     txtfile.write("----------------------------------" + "\n")
     txtfile.write(Tuple[0] + ": " + str( "{:2.2f}".format(Tuple[2]))  + "% (" + str(Tuple[1]) + ")" + "\n")
    
     textfile.close()      


   
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
    
  #Total Votes: 3521001
 # -------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
 # -------------------------
  #Winner: Khan
  #-------------