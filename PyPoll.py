import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
#    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the final vote count to the terminal.
election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
print(election_results, end="")

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# # Print the final vote count to the terminal.
#     election_results = (
#     f"\nElection Results\n"
#     f"-------------------------\n"
#     f"Total Votes: {total_votes:,}\n"
#     f"-------------------------\n")
#     print(election_results, end="")

# Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        txt_file.write(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(winning_candidate_summary)


election_data.close()
