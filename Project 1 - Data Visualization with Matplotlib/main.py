import pandas as pd

colnames = ['DATE', 'TAG', 'POSTS']
df = pd.read_csv("sample_data/QueryResults.csv", names=colnames, header=0)
