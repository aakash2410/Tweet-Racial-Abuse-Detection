import pandas as pd
from copy import copy
from nltk.tokenize import word_tokenize

"""Some assumptions for this function are that the csv or excel file will have a column named 'tweets' 
and also, there will be a '/end' string at the end of each tweet in a txt file.
"""
def read_input(file_name):
	if ".csv" in file_name:
		return pd.read_csv(file_name)

	elif ".xlsx" in file_name:
		return pd.read_excel(file_name)
	
	elif ".txt" in file_name:
		f = open(file_name, "r")
		lines = f.read()
		lines = lines.split('/end')
		lines = [tweet.strip() for tweet in lines] #removes white space and newline
		lines = [tweet.lower() for tweet in lines if tweet] #removes empty strings and lowers the case
		print(lines)
		df = pd.DataFrame(lines)
		df['tweets'] = df[0]
		return df.drop(columns = 0)

f = open('slur_word_list.txt', 'r')
slur_word_list = f.readlines()
slur_word_list = [word.strip() for word in slur_word_list] #removes white space and newline
slur_word_list = [word.lower() for word in slur_word_list if word] #removes empty strings and lowers the case
df = read_input('tweets.txt')
df['abuse_score'] = list('0'*len(df['tweets']))
print(df)
for i in range(len(df['tweets'])):
	abuse_score = 0 
	tweet = copy(df['tweets'][i])
	tweet_tokenized = word_tokenize(tweet)
	for tweet_word in tweet_tokenized:
		if tweet_word in slur_word_list:
			abuse_score +=1
	df["abuse_score"][i] = abuse_score

df.to_csv('tweet_abuse_scores.csv', index = False)

	

