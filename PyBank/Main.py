import os
import csv

# Global variables
total_months = 0
total_revenue = 0 
revenue_change = 0
previous_revenue = 0
revenue_changes = []
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""



budget_data = os.path.join("./Resources/Budget_Data.csv")
with open (budget_data, encoding="UTF-8") as file:
    csvreader = csv.reader(file, delimiter=",")

    data = list(csvreader)[1:]
    for row in data:
        total_months += 1
        total_revenue += int(row[1])

        
        
        revenue_change = int(row[1])- previous_revenue
        revenue_changes.append(revenue_change)
        previous_revenue = int(row[1])

        if revenue_change > greatest_increase:
            greatest_increase = revenue_change
            greatest_increase_month = row[0]

        if revenue_change < greatest_decrease:
            greatest_decrease = revenue_change
            greatest_decrease_month = row[0]

average_revenue_change = sum(revenue_changes[1:])/ len(revenue_changes[1:])


#show output
print("Financial Analysis")
print("-"*20)
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Change: ${average_revenue_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} \n($ {greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} \n($ {greatest_decrease})")


file_to_output = os.path.join('./Analysis/financial_report.txt')
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-"*20 + "\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Revenue: ${total_revenue}\n")
    txt_file.write(f"Average Change: ${average_revenue_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} \n($ {greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} \n($ {greatest_decrease})\n")





