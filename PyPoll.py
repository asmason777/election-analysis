#Add dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes=0

# Declare new list for total candidates received votes
candidate_options=[]

#Create dictionary to store candidate votes
candidate_votes={}

#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0


# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    
    #Read (skip) the header row
    headers=next(file_reader)

    #Print each row in the CSV file:
    for row in file_reader:
        #Add to the total vote count
        total_votes = total_votes + 1

        #Print the candidate name for each row
        candidate_name=row[2]

        #If stmt to add candidate and set votes to 0
        if candidate_name not in candidate_options:
            
            # Add candidate name with no duplicates
            candidate_options.append(candidate_name)

            # Set candidate votes to 0
            candidate_votes[candidate_name]= 0
        
        # Add a vote to candidate's count
        candidate_votes[candidate_name] +=1
    
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes)/float(total_votes)*100

    print(f"{candidate_name}: received {vote_percentage: .1f}% ({votes:,})\n")

    if (votes>winning_count) and (vote_percentage>winning_percentage):

        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"----------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"----------------------------------\n")
print(winning_candidate_summary)




# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candiadats who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on the popular vote

