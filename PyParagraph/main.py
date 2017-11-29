# This python script reads an input file, in a subdirectory called Resrouces, 
#   containing a passage and performs some basic linguistic analysis.
# After processing all the input data, it prints an approximte count of sentences,
#   words and letters along with the average letter count (per word) and sentence 
#   length (in words).
#
# Data in the input file are assumed to be ASCII text though it can also contain special
#   non-printable characters like carriage return and line feed.
#
# Results are also saved in an output file in the Resources subdirectory.
# NOTE: the output file is overwritten; if its contents are needed, either
#       save its contents to another file OR change the name of the output file. 
#
# NOTE 2: The regualar expression for detecting end of sentences does not correctly handle
#   middle initials; e.g., "Mary A. Jones went home." is parsed as two sentences. There is
#   input text containing a middle initial in paragraph_2.txt.
#   I can address middle initials by specifying: sentence_endings = "(?<=[.!?])\W\"*\s+"
#   However, this RE completely mishandles the input text in paragraph_1.txt--although it 
#   correctly processes paragraph_2.txt!
#   I am not sure why this happens; if you have any dieas, please let me know.
#   Please see additional comments below reg. the RE expression for detecting sentences.
# Dependencies
import os
import csv
import string
import re
# Initialize variables that track sentence, word and character counts.
sentence_count=0
word_count=0
char_count=0
# Open and read the input file (under Resources sub-directory).
#   Specify UTF-8 encoding to get rid of non-ASCII characters.
#   The entire input file is read into a string called passage.
input_file = os.path.join("Resources", "paragraph_2.txt")
f = open(input_file, 'r', encoding="utf-8")
passage=f.read()
# This regualr expression below does not properly handle middle initials; see NOTE 2 above.
# It does handle other more complicated cases present in paragraph_2.txt, such as the presence
#   of special formatting characters (carriage return, line feed, form feed) and sentences
#   ending within quoted text; e.g., I heard her say "hi there."
#   Handling of special formatting characters can be  handled using \s: (?<=[.!?]\s+)
#   And to properly handle sentences ending w/in quoted text: (?<=[.!?])\"*"
#   The final RE which handles both of these cases is the combination of two above REs.
# Using this RE break the entire passage into individual sentences (i.e., a list).
sentence_endings = "(?<=[.!?$])\"*\s+"
sentences=re.split(sentence_endings, passage)
# With passage broken into individual sentences, 
#   iterate over individual words in each sentence:
for sentence in sentences:
# The print statement below is very useful for debugging; so I left it as a comment.
#    print (sentences[sentence_count] + '***')
    if len(sentence) > 0:          # Check to make sure sentence is not blank/empty
        sentence_count+=1          #   and increment the sentence count
    words=re.split('\s',sentence)  # Break up a sentence into words using split()
    for word in words:             # Iterate over all the words in a sentence
      if len(word)>0:              # Check to make sure word is not blank/empty
          word_count+=1            #   and increment the word count
      char_count+=len(word)        # Increment the character count by the length of the
                                   #   current word (no need to check for empty words since
                                   #   their length is 0 anyway)
# Now that all counts are known, output a linguistic summary
print ("Paragraph Analysis\n")
print ("------------------\n")
print ("Approxiamte word count: " + str(word_count))
print ("Approximate sentence count: " + str(sentence_count))
print ("Approximate letter count : " + str(char_count/word_count))
print ("Approximate sentence length : " + str(word_count/sentence_count))
# Now output same results to the output file
# NOTE: the output file is overwritten; if its contents are needed, either
#       save its contents to another file OR change the name of the output file below
output_path = os.path.join('Resources', 'Paragraph_analysis_2.txt')
with open(output_path, 'w') as f:
  f.write ("Paragraph Analysis\n")
  f.write ("------------------\n")
  f.write ("Approxiamte word count: " + str(word_count) + "\n")
  f.write ("Approximate sentence count: " + str(sentence_count) + "\n")
  f.write ("Approximate letter count : " + str(char_count/word_count) + "\n")
  f.write ("Approximate sentence length : " + str(word_count/sentence_count) + "\n")