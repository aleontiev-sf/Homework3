# This python script reads an input csv file stored in a subdirectory called Resrouces and prints a financial summary analysis
# Data in the input file are in csv format and comprised of two columns: a date (string) and corresponding monthly revenue (number).
# These data are assumed to be unique (no duplicates) and contiguous (no gaps).
# After processing all the input data, the following summary for the period (input file) is produced:
#   Total number of months, total revenue, average monthly revenue change, greatest increase/decrease in monthly rvenue.
# The review period corresponds to data in the input file.
# To process a different file, change the file name in line 12.
#
# Import various dependencies (libraries)
import os
import csv
budget_csv = os.path.join("Resources", "budget_data2.csv") # Set the path for the input file
with open(budget_csv, newline="") as csvfile:              # Open and read the csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skip over the first line (header)
    # Initialize various variables
    total_rev=0             # The variable to track total revenue for the period (input file)
    prior_month_rev=0       # The variable to track prior month's revene (used for calculating monthly rev change)
    total_monthly_change=0  # The variable to track total monthly change (used for calculating average monthly change)
    max_monthly_rev_inc=0   # The variable to track the highest monthly revenue increase  for the period (input file)
    max_monthly_rev_dec=0   # The variable to track the highest monthly revenue decrease  for the period (input file)
    # Iterate throught each row/line of data in the input file (budget_csv)
    for row in csvreader:
        date=row[0]                 # Capture the date for current row; date is in the first column (index 0)
        total_rev+=float(row[1])    # Increment total revenue by the revenue in current row; revenue is in the second column (index 1)
        # Calculate monthly revenue change, treating the first month (row 2 in input data) as a special case since there is no prior month
        if csvreader.line_num==2:
            monthly_change=0
        else:
            monthly_change=float(row[1])-prior_month_rev
        total_monthly_change+=monthly_change # Increment total monthly revenue change by the amount of current month revenue change
        # Check to see if current monthly revenue change is higher/lower than the highest monthly increase/decrease recorded so far
        # When one of the conditions is met, update the respective variables which track the highest monthly increase/decreas
        #     and the corresponding date
        if monthly_change > max_monthly_rev_inc:
            max_monthly_rev_inc=monthly_change
            date_max_rev_inc=date
        elif monthly_change < max_monthly_rev_dec:
            max_monthly_rev_dec=monthly_change
            date_max_rev_dec=date
        # Update the prior month revenue variable to the current month revenue before moving to the next row in input date
        prior_month_rev=float(row[1])
    # We are done processing all data in the input file; start calculating and printing financial analysis results
    total_months=int(csvreader.line_num-1) # Use csvreader line_num attribute to calcualte the number of months sine each row is one record; decrement it by 1 to account for the header row
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    # In calculations and print statements below, various numeric values are cast to int in order to print a whole number
    print("Total Revenue: $" + str(int(total_rev))) 
    print("Average Revenue Change $" + str(int(total_monthly_change/total_months)))
    print("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(max_monthly_rev_inc))+")")
    print("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
           str(int(max_monthly_rev_dec)) + ")" )
# Now output the same analysis to the output file
# NOTE: the output file is overwritten; if its contents are needed, either
#       save its contents to another file OR change the name of the output file below
output_path = os.path.join('Resources', 'Financial_Analysis_2.txt')
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total Revenue: $" + str(int(total_rev)) + "\n")
    f.write("Average Revenue Change $" + str(int(total_monthly_change/total_months)) + "\n")
    f.write("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(max_monthly_rev_inc)) + ")" + "\n")
    f.write("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
           str(int(max_monthly_rev_dec)) + ")" + "\n")