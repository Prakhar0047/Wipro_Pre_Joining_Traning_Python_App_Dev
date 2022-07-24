import pandas as pd 

df = pd.read_json('data.json', orient='split')
print(df.iloc[0])