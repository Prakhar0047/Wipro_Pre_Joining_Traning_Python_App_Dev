import math
import threading
import time


class thread1(threading.Thread):
  # factorial
  def __init__(self, val1):
    super(thread1, self).__init__()
    self.val1 = val1

  def run(self) -> None:
    return math.factorial(self.val1)


class thread2(threading.Thread):
  def __init__(self, val1):
    super(thread2, self).__init__()
    self.val1 = val1

  def run(self) -> None:
    return abs(self.val1)


class thread3(threading.Thread):
  def __init__(self, val1, val2):
    super(thread3, self).__init__()
    self.val1 = val1
    self.val2 = val2

  def run(self) -> None:
    return self.val1+self.val2


obj1 = thread1(5)
obj2 = thread2(-2)
obj3 = thread3(2, 3)

t1 = obj1
t2 = obj2
t3 = obj3

a = t1.run()
b = t2.run()
c = t3.run()

print(a)
print(b)
print(c)