import pandas as pd

bios = pd.read_csv("./data/bios.csv")


# Data Transformation

# Renaming columns
# Task - Renaming 'name' to 'full name'

#bios.rename(columns={'name':'full name'}, inplace= True)
# print(bios)

# Applying Functions
# apply a lambda function to increase each age by 1 year
#bios['weight_kg'] = bios['weight_kg'].apply(lambda x : x +1)
#print(bios)

# Grouping and Aggregation
# Task - Group data by "born_country" and calculate average weight
grouped_df = bios.groupby('born_country')['weight_kg'].mean().reset_index()
print(grouped_df)

# Aggregation functions
# Calculate total and average for each region
aggregation_bios = bios.groupby('born_region')['weight_kg'].agg(['sum','mean']).reset_index()
print(aggregation_bios)