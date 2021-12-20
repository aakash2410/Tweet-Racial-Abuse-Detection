import pandas as pd

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
		df = pd.DataFrame(lines)
		df['tweets'] = df[0]
		return df.drop(columns = 0)

