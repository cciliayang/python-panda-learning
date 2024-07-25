import pandas as pd

#Create a dictionary

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	'Age': [23 , 26, 22, 45, 32],
	'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

#Convert dictionary to DataFrame
df = pd.DataFrame(data)
print(df)

#How to read a CSV file into a DataFrame
df = pd.read_csv('./data/bios.csv')
print(df.head())