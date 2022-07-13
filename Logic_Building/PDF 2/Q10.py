"""
Centred

1
121
12321
"""

s=''
height = int(input())
for x in range(1,height+1):
  s+=str(x)
  if len(s) == 1:
    print(s.center(height*2," "))
  else:
    temp = s+s[len(s)-2::-1]
    print(temp.center(height*2," "))