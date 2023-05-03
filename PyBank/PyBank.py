
import csv
from pathlib import Path

# Read CSV file
input_file = Path("Resources/budget_data.csv")
output_file = Path("financial_analysis.txt")

with input_file.open() as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

# Set Variables
    total_months = 0
    net_total = 0
    changes = []
    prev_profit_loss = None
    greatest_increase = {"date": "", "amount": float('-inf')}
    greatest_decrease = {"date": "", "amount": float('inf')}

# Loopin' to Analyze
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss

        if prev_profit_loss is not None:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        prev_profit_loss = profit_loss

    average_change = sum(changes) / len(changes)

# Create Report Summary
report = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})
"""

# Print to Terminal Box
print(report)

#Spit Out to Text File
with open("Analysis/financial_analysis.txt", "w") as txtfile:
    txtfile.write(report)