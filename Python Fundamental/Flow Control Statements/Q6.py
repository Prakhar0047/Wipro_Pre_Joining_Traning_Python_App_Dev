def prime(num1):
  if num1 > 1:
      for i in range(2, int(num1/2)+1):
          if (num1 % i) == 0:
              print(num1, "is not a prime num1ber")
              break
      else:
          print(num1, "is a prime num1ber")
  else:
      print(num1, "is not a prime num1ber")

n1 = int(input())
prime(n1)