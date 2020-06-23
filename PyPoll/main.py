#Import os module and csv module
import os
import csv

#Path for file
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
textpath =os.path.join('..','PyPoll','Analysis','election_results.txt')  

#Counting votes
total_votes = 0

#candidates list and candidates votes
candidates_list = []
candidate_votes = {}

#Winner
winner_candidate = ""
winner_count = 0

#Reading CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)
    #Read each row of data after the header
    for row in csvreader:
       #Counting number of votes
         total_votes = total_votes + 1
       #Candidates list
         candidates_name = row[2]
    #The total number of votes each candidate won
         if (candidates_name not in candidates_list):
             candidates_list.append(candidates_name)
             candidate_votes[candidates_name]= 0
            
         candidate_votes[candidates_name]=candidate_votes[candidates_name] + 1

    #Print Results 
    print("\n")
    print(f"Election Results\n")
    print(f"----------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print(f"----------------------------\n") 
    #Create text file
    with open(textpath, 'w') as txtfile:
         txtfile.write(f"Election Results\n")
         txtfile.write(f"----------------------------\n")
         txtfile.write(f"Total Votes: {total_votes}\n")
         txtfile.write(f"----------------------------\n")

    #Percentages
    for candidate in candidate_votes:
         votes = candidate_votes.get(candidate)
         vote_percentage = float(votes)/float(total_votes) * 100
         result = f"{candidate}:{vote_percentage:.3f}% ({votes})\n"
         print(result)
         with open(textpath, 'a') as txtfile:
                txtfile.write(result)
         
         
         if(votes> winner_count):
           winner_count = votes
           winner_candidate = candidate
           winner_result = f"Winner:{winner_candidate}\n"
    with open(textpath, 'a') as txtfile:
           txtfile.write(f"----------------------------\n")
           txtfile.write(winner_result)
           txtfile.write(f"----------------------------\n")
              
    #print(result)
    print(f"----------------------------\n") 
    print(winner_result)
    print(f"----------------------------\n") 
    


    