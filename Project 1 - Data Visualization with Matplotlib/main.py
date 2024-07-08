import pandas as pd

colnames = ['DATE', 'TAG', 'POSTS']
df = pd.read_csv("sample_data/QueryResults.csv", names=colnames, header=0)

# Show First Five Rows
print(df.head())
# Show Last Five Rows
print(df.tail())
# Show the Number of Rows & Columns
print(df.shape)
# Count the number of entries in each column
print(df.count())