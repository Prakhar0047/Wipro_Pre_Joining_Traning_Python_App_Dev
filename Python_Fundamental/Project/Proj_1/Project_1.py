distance = int(input("How far would you like to travel in miles?"))
if distance <3:
  print("I suggest Bicycle to your destination")
elif distance >3 and distance<300:
  print("I suggest Moter-Cycle to your destination")
else:
  print("I suggest Super-Car to your destination")