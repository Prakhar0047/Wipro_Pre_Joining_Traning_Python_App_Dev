import pandas as pd
avg = 0
df = pd.read_json('data.json')
print("This is DataFrame")
print(df)

for x in df:
  print(x)