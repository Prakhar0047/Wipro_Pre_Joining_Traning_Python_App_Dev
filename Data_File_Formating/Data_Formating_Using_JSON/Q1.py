import pandas as pd
avg = 0
df = pd.read_json('data.json')
print("This is DataFrame")
print(df)

for x in df:
  print(x)
# for x in df:
#   temp = df.loc[0, x]
#   print(temp)
#   avg+=int(temp)
# print(avg)