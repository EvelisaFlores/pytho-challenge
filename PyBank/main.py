#Import os module and csv module
import os
import csv

#Path for file
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
textpath =os.path.join('..','PyBank','Analysis','financial_analysis.txt')  

#Create Lists
pl_changes = []

#Variables
count_months = 0
total_pl = 0
previous_pl = 0
total_pl_change = 0
monthly_changes_pl = 0
average_change = 0

greatest_increase = 0
greatest_decrease = 0
g_increase_date = [""]
g_decrease_date = [""]

#Reading CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   #Read the header row first
    csv_header = next(csvreader)
    #Read each row of data after the header
    for row in csvreader:
        count_months = count_months + 1       #Count the number of months
        total_pl = total_pl + int(row[1])     #Calcualte Net Total Amount in Profit/Losses 
        #Calcualte Profit and Losses change by month
        current_pl = int(row[1])
        monthly_changes_pl = current_pl - previous_pl  #Calcualte Profit/Losses monthly changes
        previous_pl =  current_pl
        #Calculate average of the monthly changes in Profit/Losses
        if(count_months != 1): #how to calculate total_pl_change eliminating monthly_changes_pl results 0???????    #and monthly_changes_pl !=0
            pl_changes.append(monthly_changes_pl)  
            total_pl_change = total_pl_change + monthly_changes_pl
            #average_change = round(total_pl_change/count_months,2) 
            average_change = round(total_pl_change/len(pl_changes),2)
                         #print(len(pl_changes)) 
        #Greatest Increase
        if(monthly_changes_pl > greatest_increase):
            greatest_increase = monthly_changes_pl
            g_increase_date = (row[0])
        #Greatest Decrease
        if(monthly_changes_pl < greatest_decrease):
            greatest_decrease = monthly_changes_pl
            g_decrease_date = (row[0])
          
    #Print Results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" + str(count_months))
    print("Total Revenue:" + "$" + str(total_pl))
    print("Average Change:" + "$" + str(average_change))
    print("Greatest Increase:" + str(g_increase_date) + " ($" + str(greatest_increase) + ")" )    
    print("Greatest Decrease:" + str(g_decrease_date) + " ($" + str(greatest_decrease) + ")" ) 
    
with open(textpath, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Months:" + str(count_months))
    txtfile.write("\n")
    txtfile.write("Total Revenue:" + "$" + str(total_pl))
    txtfile.write("\n")
    txtfile.write("Average Change:" + "$" + str(average_change))
    txtfile.write("\n")
    txtfile.write("Greatest Increase:" + str(g_increase_date) + " ($" + str(greatest_increase) + ")" )
    txtfile.write("\n")
    txtfile.write("Greatest Decrease:" + str(g_decrease_date) + " ($" + str(greatest_decrease) + ")" ) 
        
        

       

 