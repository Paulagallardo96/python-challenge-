

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:56:25 2018

@author: paulaamandagallardo
"""

import os
import csv

mypath = "/Users/paulaamandagallardo/Desktop/DataAnalyticsGW/Python/python-challenge/python-challenge-/PyBank"
csvpath = os.path.join(mypath, 'budget_data.csv')

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
        
    count = 0
    
    total = 0
    diffs = []
    #diffThisMonth1 = 0
    firstFlag = True
    
    for row in csvreader:
        row = row[0].split(",")
        print(row)
        count = count + 1
        
        amount = int(row[1])
        total += amount 
        
        #diffThisMonth = int(row[1])
        #diffThisMonth1 += diffThisMonth
        
        # do this line only if we've already been through the loop at least once
        if firstFlag == False:
            
            #add a new entry to diffs equal to the diff between this months amount and last months
            diffThisMonth = amount - amountLastMonth
            diffs.append(diffThisMonth)
        else:
            # Record the fact that we've been through the loop once
            firstFlag = False
        
        amountLastMonth = amount 

        
        #diffThisMonth = int(row[1])
        #diffThisMonth1 += int(diffThisMonth)
        
        Total_diffThisMonth = sum(diffs)
    
    average = Total_diffThisMonth / (count - 1)
        
        #average = total / count
    
        #diffThisMonth = amount - amountLastMonth
        #diffs.append(diffThisMonth)
        #add a new entry to diffs equal to the diff between this monts amount and last months
        
        ##amountLastMonth = amount 
        
        #The greatest increase in profits (date and amount) over the entire period
        
        
    GreatesIncreaseIncome = max(diffs)
        
        #The greatest decrease in losses (date and amount) over the entire period
        
    GreatedDecreaseIncome = min(diffs)
        
        
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average}')
    print(GreatesIncreaseIncome)
    print(GreatedDecreaseIncome)
    
    #print(mean(diffs))