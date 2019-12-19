import os
import csv

election_data_csv = os.path.join('..' , 'python-challenge' , 'election_data.csv')

Candidates = {}
Total_Votes = 0
Max_Votes = 0
Winner = ""

with open(election_data_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvfile)
    
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        Candidate = row[2]
        if Candidate in Candidates:
            Candidates[Candidate] = Candidates[Candidate] +1 
        else:
            Candidates[Candidate] = 1
outputPath = os.path.join('..','python-challenge', 'PyPoll.txt')
file=open(outputPath, 'w')

print ("Election Results")
file.write("Election Results" + "\n")
print ("Total Votes: ",Total_Votes)
file.write(f"Total Votes {Total_Votes}" +"\n")
for Candidate, num in Candidates.items(): 
    print(Candidate + ": " + str(num) + " " + str(round((num / Total_Votes) *100,2)) + "%")
    file.write(Candidate + ": " + str(num) + "\n"+ str(round((num / Total_Votes)*100)) + "% " "\n")
for Candidate, numofvotes in Candidates.items():
        if (num > Max_Votes):
            Max_Votes = num 
            Winner = Candidate
print(f"Winner {Winner}")
file.write(f"Winner {Winner}")
file.close() 
