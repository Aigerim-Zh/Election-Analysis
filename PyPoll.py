# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
# Make sure that the folder "Analysis" is created
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a Total Vote Counter
total_votes = 0

# Set a list with the candidates' names
candidate_options = []

# Declaring an empty dictionary to count the votes for each candidate
# where the key is the candidate name and the value is the number of votes 
candidate_votes = {}

# Set a winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Reading the "election_results.csv" file using the csv module with the reader function
    # The "file_reader" variable is referencing the file object stored in the memory
    file_reader = csv.reader(election_data)

    # To iterate through each row, we need to skip the header or the column name
    # We can do it using the next() function to read the header row
    headers = next(file_reader)
      #print(headers)
    # Printing each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes +=1 

        # Print the candidate name from each row 
        # the Candidate Name is the 3rd column, and, thus, has index 2
        candidate_name = row[2]

        # Get unique candidate names

        # If the candidate name does not match any existing candidate names
        if candidate_name not in candidate_options:
            # Then, add it to the list of candidates 
            candidate_options.append(candidate_name)

            # Start tracking that candidate's vote count
            # we do this inside the if statmenet since we want to initialize the count 
            # for unique candidate names only as keys
            # ???? WHY EXACTLY THIS IS INSIDE THE IF-STATEMENT
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'------------------------\n')
    print(election_results, end ="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
            # votes for each candidate equal to the values of the candidate_votes dictionary
            votes = candidate_votes[candidate_name]
            # calculating the percentage of votes for each candidate
            votes_percentage = (float(votes)/float(total_votes)) * 100
            candidate_results = (
                f'{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n'
            )
            # print the vote count and percentage for each candidate
            print(candidate_results)
            txt_file.write(candidate_results)

            # Determine the winning vote count and candidate by the number and percentage votes
            if (votes > winning_count) and (votes_percentage > winning_percentage):
                # If true, then set winning count = votes and winning_percentage = votes_percentage 
                winning_count = votes
                winning_percentage = votes_percentage
                # and set the winning_candidate = candidate_name
                winning_candidate = candidate_name
            # Printing the candidate name and percentage of votes
        # candidate_results = (f'{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n')

    winnning_candidate_summary = (
            f'--------------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'--------------------------\n'
            )
            
    print(winnning_candidate_summary)
    txt_file.write(winnning_candidate_summary)


