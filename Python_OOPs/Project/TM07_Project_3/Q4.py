import math

class myMath:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def addition(self):
    return self.a+self.b

  def subs(self):
    return self.a-self.b

  def multiply(self):
    return self.a*self.b

  def diviison(self):
    if self.b == 0:
      print("Not Possible")
    else:
      return self.a/self.b

  def sqroot(self):
    return math.sqrt(self.a)


obj = myMath(2,5)
print(obj.addition())
print(obj.subs())
print(obj.multiply())
print(obj.diviison())
print(obj.sqroot())
