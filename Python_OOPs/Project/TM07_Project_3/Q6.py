# Python Program illustrate how
# to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, o):
		return self.a - o.a
ob1 = A(10)
ob2 = A(2)

print(ob1 + ob2)
