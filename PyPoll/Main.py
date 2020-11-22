import os
import csv

# Global variables
total_votes = 0 
candidate_list = []
candidate_dictionary = {}
vote_dictionary = {}

election_data = os.path.join("./Resources/election_data.csv")

with open (election_data, encoding="UTF-8") as file:
    candidate_dictionary = list(csv.DictReader(file)) 
    #print(candidate_dictionary[1:10])
    for row in candidate_dictionary: 
        if row['Candidate'] not in candidate_list:
            candidate_list.append(row['Candidate'])
            vote_dictionary.update({row['Candidate']: 1})
        else:
            vote_dictionary[row['Candidate']] += 1


votes_list = [total_votes + value for key, value in vote_dictionary.items()]
total_votes = sum(votes_list)
max_votes = max(votes_list)
winner = ""

def percent_vote(value):
    return (value/total_votes)*100
#show results

print(f"Election Results")
print('-'*20)
print(f"Total votes: {total_votes}")
print('-'*20)
for key, value in vote_dictionary.items():
    print(f"{key} : {percent_vote(value):.3f}% ({value})")
    if(value == max_votes):
        winner = key
print('-'*20)
print(f"Winner : {winner}")
print('-'*20)


file_to_output = os.path.join('./Analysis/Election_result.txt')
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write('-'*20 + "\n")
    txt_file.write(f"Total votes: {total_votes}\n")
    txt_file.write('-'*20 + "\n")
    for key, value in vote_dictionary.items():
        txt_file.write(f"{key} : {percent_vote(value):.3f}% ({value})\n")
        if(value == max_votes):
            winner = key
    txt_file.write('-'*20 + "\n")
    txt_file.write(f"Winner : {winner}\n")
    txt_file.write('-'*20)


