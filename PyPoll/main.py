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
candidates = {}               # Declare a dictionary called candidates
                              #   index candidate name, value vote count
election_csv = os.path.join("Resources", "election_data_2.csv")
with open(election_csv, newline="") as csvfile:
  csvreader = csv.reader (csvfile, delimiter=",")
  next (csvreader)            # Skip over the first line (the header)
  for row in csvreader:       # For every row in the input file check to see:
    if row[2] in candidates:  #   If the current candidate exists in the candidates dict
      candidates[row[2]] += 1 #     if so, increment her/his vote count
    else:                     #   otherwise
      candidates[row[2]] = 1  #     initialize her/his vote to 1
total_votes = csvreader.line_num - 1  # Total number of votes is the number of lines 
                                      #    in input file minus 1 (header line)
print ("Election Resuls\n")
print ("--------------------------\n")
print ("Total Votes: " + str(total_votes))
print ("\n--------------------------\n")
for key, value in candidates.items(): # This loop prints voting results for each candidate
                                      #  key is candidate name, value is the vote count
  print (key + ": " + "{0:.1f}%".format(value/total_votes * 100) + 
         " (" + str(value) + ")")
print ("\n--------------------------\n")
print ("Winner: " + max(candidates, key=candidates.get) ) # determine the winner using 
print ("\n--------------------------")                                                          #    max method 
# Now output same results to the output file
# NOTE: the output file is overwritten; if its contents are needed, either
#       save its contents to another file OR change the name of the output file below
output_path = os.path.join('Resources', 'Election_results_2.txt')
with open(output_path, 'w') as f:
  f.write ("Election Resuls\n")
  f.write ("--------------------------\n")
  f.write("Total Votes: " + str(total_votes) + '\n')
  f.write ("\n--------------------------\n")
  for key, value in candidates.items():
    f.write(key + ": " + "{0:.1f}%".format(value/total_votes * 100) + 
            " (" + str(value) + ")\n")
  f.write ("\n--------------------------\n")
  f.write("Winner: " + max(candidates, key=candidates.get) + '\n')
  f.write ("\n--------------------------")