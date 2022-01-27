# Election-Analysis using Python

## Overview of the Project

### Background information 
There are **three main voting methods**:
- Mail-In Ballots are hand-counted at the central office.
- Punch Cards are collected and then fed into a machine that tabulates votes totals and sends the results to the central office.
- Direct Recording Electronic (DRE) counting machines. The DRE memory cards are sent to the central office and counted by a computer. 

The votes cast by these three methods will determine the election results. 

### Purpose 

This case study analysis is focused on helping a Colorado Board of Elections employee to conduct an audit of tabulated Congressional Election results in the state. The audit method developed in this project can be applied to assessing the results of other elections in the state. We are specifically tasked with determining the following: 

- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote

The election commission has requested some additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

### Resources
 - **The dataset** consists of 369,711 observations, representing numbers for the  Ballot ID, a name for the County, and Candidate columns. The original data is in the CSV format and can be found [here](https://github.com/Aigerim-Zh/Election-Analysis/blob/main/Resources/election_results.csv).
 - **The code for the analysis** can be found [here](https://github.com/Aigerim-Zh/Election-Analysis/blob/main/PyPoll_Challenge.py).
 - This audit can be done in Excel but this project tries to automate the process using **Python 3.7.6 64 bit, coded through VSCode 1.63.2.**

## Election Audit Results

- There are 369,711 votes cast in total. 
- There are three counties in this election with the following results:
    - Arapahoe received 6.7% of the total votes with 24,801 votes.
    - Jefferson received 10.5% of the total votes with 38,855 votes.
    - **Denver had the largest number of 306,055 votes, accounting for 82.8% of the total votes.**
- There are three candidates in this election with the following results:
    - Raymon Anthony Doane received 3.1% of the total votes with 11,606 votes.
    - Charles Casper Stockham received 23.0% of the total votes with 85,213 votes.
    - **Diana DeGette won the election with 272,892 votes, accounting for 73.8% of the total votes.**

## Election-Audit Summary
The script developed in this project can be applied to auditing other elections. Elections in other states can be audited as long as the dataset has three columns of the Ballot ID, County Name, and Candidate Name. The order of these columns must be preserved, otherwise  lines 52 and 55 of the code need to be modified for the correct index inside the row function:

    ```
    # Get the candidate name from each row.
    candidate_name = row[2] # the Candidate Name is the 3rd column, and, thus, has index 2

    # 3: Extract the county name from each row.
    county_name =  row[1] # County Name is the 2nd column, and, thus, has index 1
    ```
The dataset name can be changed in line 9: 
    
    ```
    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    ```
However, the file has to be in the CSV format, otherwise, line 38 needs to be changed to read an excel file or other data type.

    ```
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
    ```

To write election results in the text file makes sure to create an Analysis folder in your repository, where you will save the file:

    ```
    # Add a variable to save the file to a path.
    # Make sure that the folder "Analysis" is created
    file_to_save = os.path.join("Analysis", "election_analysis.txt")
    ```