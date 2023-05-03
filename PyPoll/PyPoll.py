
import csv
from collections import defaultdict
from pathlib import Path

# Read CSV file
input_file = Path("Resources/election_data.csv")
output_file = Path("election_results.txt")

total_votes = 0
candidates = defaultdict(int)

with input_file.open() as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

    for row in reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] += 1

# Calculate Votes and Pinpoint Winner
winner = {"name": "", "votes": 0}
formatted_candidates = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    formatted_candidates.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Set Up Analysis Report
report = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Candidates: {', '.join(formatted_candidates)}
-------------------------
Winner: {winner["name"]}
-------------------------
"""

# Print to Terminal Box
print(report)

#Spit Out to Text File
with open("Analysis/election_results.txt", "w") as txtfile:
    txtfile.write(report)
