import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]

like = list(num1.split("-"))
unlike = list(num2.split("-"))
ca = list(num3.split("-"))
happiness = 0

for x in ca:
  if x in like:
    happiness += 1
  elif x in unlike:
    happiness -= 1
  else:
    pass

print(happiness)