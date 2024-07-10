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

#Convert Entire Column to Datetime
df.DATE = pd.to_datetime(df.DATE)
print(df.head)

# use pivot table
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
print(reshaped_df)

#DataFrame Dimension
print(reshaped_df.shape)

#DataFrame HEAD & TAIL
print(reshaped_df.head())
print(reshaped_df.tail())

#DataFrame Column Name
print(reshaped_df.columns)

