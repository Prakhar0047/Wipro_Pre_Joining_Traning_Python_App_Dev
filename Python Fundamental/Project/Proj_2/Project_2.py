print("How much does it cost to operate one server per day?")
print("$",24*0.51)
print("How much does it cost to operate one server per week?")
print("$",7*24*0.51)
print("How much does it cost to operate one server per month?")
print("$",4*7*24*0.51)
print("How much days can I operate one server with $918?")
x = 918
count=0
while x>0:
  x-=24*0.51
  count+=1
print(count)