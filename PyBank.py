import os
import csv

budget_data_csv = os.path.join('..' , 'python-challenge' , 'budget_data.csv')

Number_of_Months = 0
Net_Total = 0
Average_Change = 0
Previous = 0
Net_Change = 0
Total_Net_Change = 0
Greatest_Change = 0
Greatest_Decrease = 0

with open(budget_data_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvfile)

    for row in csvreader:
        Net_Total = Net_Total +int(row[1])
        Number_of_Months = Number_of_Months + 1 
        if Number_of_Months > 1:
            Net_Change = int(row[1]) - Previous
        Previous = int(row[1])
        Total_Net_Change = Total_Net_Change + Net_Change 
        
        if Net_Change > Greatest_Change:
            Greatest_Change = Net_Change
            Greatest_Date = row[0]
        if Net_Change < Greatest_Decrease:
            Greatest_Decrease = Net_Change
            Worst_Date = row[0]

Average_Change = Total_Net_Change / (Number_of_Months - 1)

print("Total Months: " , Number_of_Months)
print("Total: $",Net_Total)
print("Average Change: $",round(Average_Change))
print ("Greatest Increase in Profits: ", Greatest_Date , "$",Greatest_Change)
print ("Greatest Decrease in Profits: ", Worst_Date , "$",Greatest_Decrease)

outputPath = os.path.join('..','python-challenge', 'PyBank.txt')
file=open(outputPath, 'w')
file.write("Total Months: " + str(Number_of_Months))
file.write("Total: $" + str(Net_Total))
file.write("Average Change: $" + str(round(Average_Change)))
file.write("Greatest Increase in Profits" + str(Greatest_Date) + "$" + str(Greatest_Change))
file.write("Greatest Decrease in Profits" + str(Worst_Date) + "$" + str(Greatest_Decrease))
file.close()