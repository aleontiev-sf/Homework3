# This python script reads an input csv file, in a subdirectory called Resrouces, 
#   containing employee data, transforms various fields and produces an output csv
#   file, in the Resources subdirectory.
# Data in the input file are in csv format and comprised of five fields (all strings): 
#   ID, full name, date of birth (YYYY-MM-DD), SSN (all digits), state (full name).
# To process a different file, change the input file name in line 34.
# The script produces an output csv file comprised of six fields (all strings):
#   ID, first name, last name, date of birth (DD/MM/YYYY), SSN (masked), state (abbreviated).
# NOTE: the output file is overwritten; if its contents are needed, either save
#   the contents to another file OR change the name of the output file in line 60.
#
# Dependencies
import os
import csv
import re
import datetime
from datetime import datetime
state_abbr = {      # State abbreviation dictionary: key is state full name, value is two-letter abbreviation
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
new_emp_dict = [] # Declare an empty list which will contain all transfomred records
# Create the path for the input file, open it and read csv records
employee_csv = os.path.join("Resources", "employee_data2.csv")
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip over the first line (header)
    # Iterate throught each row/line of data in the input file
    for row in csvreader:
        # Store various fields in the input row into variables for subsqequent transformation
        emp_id = str(row[0])
        emp_name = row[1]
        emp_dob = row[2]
        emp_ssn = row[3]
        emp_state = row[4]
        # Start transformation of the name, DOB, SSN masking and state abbreviation
        first_name,last_name = emp_name.split()          # Split full name into first and last name
        date_obj = datetime.strptime(emp_dob,'%Y-%m-%d') # Save input date in an object specifying YYYY-MM-DD format
        new_date = date_obj.strftime('%d/%m/%Y')         # Convert date object using DD/MM/YYYY format
        ssn_last4 = emp_ssn[-4:]                         # Save last 4 SSN digits via backward slicing
        new_ssn = "***-**-" + ssn_last4                  # Form new SSN by exposing only last 4 digits
        new_state = state_abbr[emp_state]                # Look up abbreviated state name in dictionary
        # Create a new row using trasnfomred fields above, and append it to the list that will
        #    eventually contain all transformed records
        new_rec = emp_id + "," + first_name + "," + last_name + "," + new_date + "," + new_ssn + "," + new_state
        new_emp_dict.append(new_rec)
# Now that all input records have been converted and saved in a list, output them to an output csv file
# NOTE: the output file is overwritten; if its contents are needed, either save
#   the contents to another file OR change the name of the output file below.
output_file = os.path.join("Resources", "Converted-2.csv")
with open (output_file, 'w') as f:
    writer = csv.writer(f)
    # Write the header row (titles of various fields)
    writer.writerow(['Emp ID', 'First name', 'Last name', 'DOB', 'Masked SSN', 'State'])
    # Output all the converted rows previosuly stored in a list
    # Since the csv writerow method appends commas automatically to each field, remove
    #   commas from the row (using split)
    for i in range(len(new_emp_dict)):
       writer.writerow(re.split(',', new_emp_dict[i]))

