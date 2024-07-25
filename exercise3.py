import pandas as pd

bios = pd.read_csv("./data/bios.csv")


#Data Cleaning

#Assume 'bios.csv' has some missing values
#Task - fill missing values with a default value
bios.fillna("Unknown", inplace= True)
print(bios.head())

#Removing Duplicates
#Task - Remove duplicate rows from the DataFrame
bios.drop_duplicates(inplace= True)
print(bios)