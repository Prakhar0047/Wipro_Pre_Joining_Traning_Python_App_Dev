import pandas as pd 
data = {
  "calories": [420, 380, 390], # Calories Column [Data]
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
df.to_excel('data.xlsx')