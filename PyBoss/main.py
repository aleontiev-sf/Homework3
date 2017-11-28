# This python script reads an input file, in a subdirectory called Resrouces, 
#   containing voting results.
# After processing all the input data, it prints the total number of votes, the percentage 
#   of votes and total votes for each candidate, as well as the overall winner.
# Data in the input file are in csv format and comprised of three columns (all strings): 
#   voter ID, county and candidate.
# Input data (rows) are assumed to be unique (no duplicates) and contiguous (no gaps).
# To process a different file, change the input file name in line 18.
# Results are also saved in an output file in the Resources subdirectory.
# NOTE: the output file is overwritten; if its contents are needed, either
#       save its contents to another file OR change the name of the output file. 
#
# Dependencies
import os
import csv
import string
import datetime
from datetime import datetime
state_abbr = {      # dictionary indexed by full name, value 2 letter abbreviation
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY',
    'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 
    'Wisconsin': 'WI', 'Wyoming': 'WY',}
new_emp_dict = {}  # Declare an empty dictionary which will contain transfomred records
employee_csv = os.path.join("Resources", "employee_data1.csv")
# Open and read csv
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skip over the first line (header)
    # Iterate throught each row/line of data in the input file
    for row in csvreader:
        # Store various fields in input rows into variables for subsqequent transformation
        emp_id = str(row[0])
        emp_name = row[1]
        emp_dob = row[2]
        emp_ssn = row[3]
        emp_state = row[4]
        # Start transformations of the name, DOB, SSN masking and state abbreviation
        first_name,last_name = emp_name.split()
        date_obj = datetime.strptime(emp_dob,'%Y-%m-%d') # Input date format YYYY-MM-DD
        new_date = date_obj.strftime('%d/%m/%Y')         # Output format DD/MM/YYYY
        ssn_last4 = emp_ssn[-4:]
        new_state = state_abbr[emp_state]
#        print(emp_id + "," + first_name + "," + last_name + "," + new_date + 
#          ",***-**-" + ssn_last4 + "," + new_state)
        new_emp_dict[emp_id].append(first_name)
        new_emp_dict[emp_id].append(last_name)
        new_emp_dict[emp_id].append(new_date)
        new_emp_dict[emp_id].append(ssn_last4)
        new_emp_dict[emp_id].append(new_state)
print("\nProcessed " + str (csvreader.line_num-1) + " records.")

