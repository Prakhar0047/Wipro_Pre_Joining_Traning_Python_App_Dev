# Sun is Even or Odd

def sum_odd_even(num1,num2):
  s = num1+num2
  if s%2 == 0:
    print("Even")
  else:
    print("Odd")

n1 = int(input())
n2 = int(input())
sum_odd_even(n1,n2)