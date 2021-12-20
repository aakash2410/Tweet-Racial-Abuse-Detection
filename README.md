# Tweet-Racial-Abuse-Detection
We here identify racial abuse on twitter by telling the degree of profanity in each tweet by using a set of words as a means to detect and score the extent of racial profanity.

## Some assumptions made while programming:
 1. Tweets will be processed from .csv, .xlsx or .txt file.
 2. If tweets are in txt file, they end with a "/end" string.
 3. If tweets are in csv or excel file, the tweets will be under a column name "tweets".
 4. Set of slur words will be given a text file named slur_word_list.txt where every slur word is written on a new line.

## Requirements:
1. pandas 
2. copy

## To run this program after downloading:
1. Install the requirements
2. Set up the files required (slur_word_list.txt and the file containing the tweets) in the project directory
3. Go to CMD in the project directory
4. enter the command "python slur_check.py <file_name>"
