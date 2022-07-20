import math

class myMath:
  def addition(self,a,b):
    return a+b

  def subs(self, a, b):
    return a-b

  def multiply(self, a, b):
    return a*b

  def diviison(self, a, b):
    if b == 0:
      print("Not Possible")
    else:
      return a/b

  def sqroot(self, a):
    return math.sqrt(a)

obj = myMath()
print(obj.addition(2,5))
print(obj.subs(2,5))
print(obj.multiply(2,5))
print(obj.diviison(2,5))
print(obj.sqroot(5))