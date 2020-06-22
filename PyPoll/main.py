#Import os module and csv module
import os
import csv

#Path for file
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
#textpath =os.path.join('..','PyPoll','Analysis','election_results.txt')  


count_votes = 0
#candidates = 0
candidates_list = []
candidate_votes = {}
votes_percentage = 0
votes = 0
winner = ""
winning_votes = 0

#Reading CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)
    #Read each row of data after the header
    for row in csvreader:
       #Counting number of votes
         count_votes = count_votes + 1
       #Candidates list
         candidates_name = row[2]
    #The total number of votes each candidate won
         if (candidates_name not in candidates_list):
             candidates_list.append(candidates_name)
             candidate_votes[candidates_name]= 0
         else:
             candidate_votes[candidates_name]=candidate_votes[candidates_name] + 1
   
         for candidates_name in candidate_votes:
             votes = candidates_votes.get(candidates_name)
             votes_percentage = float(votes/float(count_votes)*100
    #winner
             if (votes > winning_votes):
                 
 



   # for candidates in candidates_with_votes_list:
      #  percentage_votes_won = (candidate_votes[candidates]/votes)*100
       # print(candidates_votes)

    print("Election Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {votes}\n")
    print("-------------------------\n")
    print(percentage_votes_won)
    
            
            
       
        

       

        