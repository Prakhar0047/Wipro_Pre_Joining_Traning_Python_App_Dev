class circle:
  def __init__(self, radius):
    self.radius = radius

  def circum(self):
    return 2*3.14*self.radius

  def area(self):
    return 3.14*self.radius*self.radius


c = circle(4)
print(c.circum())
print(c.area())
