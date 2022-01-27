# Election-Analysis using Python

## Overview of the Project

### Background information 
There are **three main voting methods**
- Mail-In Ballots are hand-counted at the central office
- Punch Cards are collected and then fed into a machine that tabulates votes totals and sends the results to the central office
- Direct Recording Electronic (DRE) counting machines. DRE memory cards are sent to the central office and counted by a computer. 

The votes cast by these three methods will determine the election results. 

### Purpose 

This case-study analysis is focused on helping a Colorado Board of Elections employee to conduct audit of tabulated Congressional Election results in the state. The audit method developed in this project can be applied to asessing results of other elections in the state. We are specifically tasked with determining the following: 

- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote

### Dataset
The dataset consists of 369,711 observations, representing numbers for the  Ballot ID, a name for the County, and Candidate columns. The original data is in the CSV format and can be found [here](https://github.com/Aigerim-Zh/Election-Analysis/blob/main/Resources/election_results.csv).

### Code
Please find the code for this part of the analysis [here]
### Software 
This audit can be done in Excel but this project tries to automate the process using Python 3.7.6 64 bit, coded through VSCode 1.63.2. 

## Analysis Results

- There are 369,711 votes in total. 

- There are three candidates in this election:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidates received the following percentage and number of votes:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
    - Diana DeGette, who recived 73.8% of the total votes with 272,892 number of votes.

## Challenge Overview (Additional Analysis)
The election commission has requested some additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout
## Challenge Summary