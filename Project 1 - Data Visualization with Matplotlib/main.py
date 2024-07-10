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
# Count the entries by Group
print(df.groupby("TAG").sum())
# Count the entries
print(df.groupby("TAG").count())

# GET the entry with the highest count
print(pd.to_datetime(df["DATE"][1]))
print(type(pd.to_datetime(df["DATE"][1])))
# print(df.iloc[df.groupby("TAG").size().argmax()])