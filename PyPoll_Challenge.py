# -*- coding: UTF-8 -*-

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
all_counties = []
county_voting_info ={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_name = ""
largest_county_turnout_count = 0
largest_county_voting_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row. Each row is an array. Each colomn is an element in the array. The 3rd element of the array is a the candidate. Array starts at a count of 0.
        candidate_name = row[2]

        # 3: Extract the county name from each row. County is the 2nd element aka 1st index of the row

        county_name = row[1]

        # If the candidate does not match any existing candidate in canditate options array add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list. 
            # candidate_options is an array of unique candidate name 
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            # creates a new key in the candidate_votes object with the candidate_name 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        # The value of the new kwy is the count of how many that candidate receviced
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in all_counties:
            
            # 4b: Add the existing county to the list of counties.
            all_counties.append(county_name)

            # 4c: Begin tracking the county's vote count
            county_voting_info[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_voting_info[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name_key, county_count_value in county_voting_info.items():

        # 6b: Retrieve the county vote count.

            # Using a obj forloop so the value is county_count_value

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_count_value) / float(total_votes) * 100
        county_results = (
            f"{county_name_key}: {county_vote_percentage:.1f}% ({county_count_value:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_count_value > largest_county_turnout_count):
            largest_county_turnout_count = county_count_value
            largest_county_name = county_name_key
            largest_county_voting_percentage = county_vote_percentage
        

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_voting_summary = (
        f"-------------------------\n"
        f"Largest Voting County: {largest_county_name}\n"
        f"Largest County - Total Voter Turnout Count: {largest_county_turnout_count:,}\n"
        f"Largest County Voting Percentage Out Of All Counties: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(largest_county_voting_summary)
    

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_voting_summary)
