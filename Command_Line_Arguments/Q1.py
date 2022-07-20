"""
Example
# Importing sys is imporatant to use Command Line Argument
import sys
n1 = sys.argv[1] # It will take 1st argumenrt as it's input
print("N1: ",n1)
n2 = sys.argv[2] # It will take 2nd argumenrt as it's input
print("N1: ",n2)
# These input just like normal will be considered str so we need to convert them else they will be concatinated.
n1=int(n1)
n2=int(n2)
print(n1+n2)
"""
import sys
sum = 0

for x in range(1,len(sys.argv)):
  sum+=int(sys.argv[x])
print(sum)