import sys

n = len(sys.argv)
print("Toatal Numeber Of Args",n)

for i in range(1,n):
  print(sys.argv[i], end = " ")

Sum = 0
for i in range(1,n):
  Sum += int(sys.argv[i])

print("Result:",Sum)