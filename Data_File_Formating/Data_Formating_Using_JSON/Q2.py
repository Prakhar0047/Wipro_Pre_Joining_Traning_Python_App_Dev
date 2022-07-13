import pandas as pd 
data = {
  "Name": ["Prakhar", "Prakhar 2", "Prakhar 3", "Prakhar 4"], # Calories Column [Data]
  "Maths": [50, 40, 45, 60],
  "English": [50, 40, 45, 60],
  "Hindi": [50, 40, 45, 60],
  "French": [50, 40, 45, 60],
}

df = pd.DataFrame(data)
df.to_json('data.json')

df2 = pd.read_json('data.json')
print(df2)