
import os


import csv


import statistics

total_votes = 0
khan_wins = 0
correy_wins = 0
li_wins = 0
otooley_wins = 0

csvpath = os.path.join('election.csv')

with open(csvpath, newline="") as csvfile:

   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)

   for row in csvreader:
       total_votes+=1

col1 = set()

with open(csvpath, 'r', newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)
   for row in csvreader:
       col1.add(row[2])



with open(csvpath, 'r', newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)

   most_votes=(str(row[2]) for row in csvreader)
   popular_vote=statistics.mode(most_votes)




with open(csvpath, 'r', newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)

   for row in csvreader:
       if row[2]=='Khan':
           khan_wins+=1

       elif row[2]=='Correy':
           correy_wins+=1

       elif row[2]=='Li':
           li_wins+=1

       elif row[2]=="O'Tooley":
           otooley_wins+=1



khan_percentage = round((khan_wins/total_votes)*100,2)

correy_percentage = round((correy_wins/total_votes)*100,2)

li_percentage = round((li_wins/total_votes)*100,2)

otooley_percentage = round((otooley_wins/total_votes)*100,2)

#Export a text file with the results
election_results = (
   " \n"
   "Election Results\n"
   " \n"
   "--------------------------------------------------------------------\n"
   " \n"
   f'Total Votes:{total_votes}\n'
   " \n"
   "--------------------------------------------------------------------\n"
   f"Khan:    {khan_percentage}, {khan_wins}\n"
   f'Correy:  {correy_percentage}, {correy_wins}\n'
   f'Li:      {li_percentage}, {li_wins}\n'
   f"O'Tooley: {otooley_percentage}, {otooley_wins}\n")

print(election_results)

file_to_output = "election_results.txt"
with open(file_to_output,"w") as txt_file:
   txt_file.write(election_results)