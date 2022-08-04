# Smallest Divisor
n = int(input())
l = []
for x in range(2,n+1):
  if n%x == 0:
    l.append(x)

print(min(l))