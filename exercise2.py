import pandas as pd

#importing bios file
bios = pd.read_csv("./data/bios.csv")

#Selecting columns
# Task: Select the 'Name' And 'Weight' Columns from the DataFrame

selected_columns = bios[['name', 'weight_kg']]
print(selected_columns)

#Filtering Rows
#Task - Filter the DataFrame to include only rows where 'Weight' is greather than 70
filtered_df = bios[bios['weight_kg'] > 70]
print(filtered_df)

