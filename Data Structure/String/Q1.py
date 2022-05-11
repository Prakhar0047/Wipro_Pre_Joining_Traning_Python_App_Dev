st = "WipRo"
up=0
low=0
for x in st:
  if x.isupper() == True:
    up+=1
  else:
    low+=1

print("Upper Aplhabet",up)
print("Lower Aplhabet",low)