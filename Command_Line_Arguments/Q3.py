import sys
sum = 0

for x in range(1, len(sys.argv)):
  temp = int(sys.argv[x])
  if temp > 1:
   # check for factors
   for i in range(2, temp):
       if (temp % i) == 0:
           break
   else:
      sum += temp
print(sum)