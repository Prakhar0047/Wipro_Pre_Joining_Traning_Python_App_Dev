class distance:
  def __init__(self, x=5,y=5):
    self.ft=x
    self.inch=y

  def __lt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return "first object smaller than other"
    else:
      return "first object not smaller than other"

  def __gt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return "first object greater than other"
    else:
      return "first object not greater than other"

d1=distance(5,5)
d2=distance()
print (d1>d2)
d3=distance()
d4=distance(6,10)
print (d1<d2)
d5=distance(3,11)
d6=distance()
print(d5<d6)