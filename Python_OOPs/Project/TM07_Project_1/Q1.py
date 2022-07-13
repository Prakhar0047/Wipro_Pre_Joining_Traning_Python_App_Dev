class Employee:    
  emp_list = []

  def add_emp(self,emp_id,name,age,salary):
    self.emp_list.append([emp_id,name,age,salary])
  
  def display_emp(self):
    for x in range(len(self.emp_list)):
      print("----Report----")
      print(*self.emp_list[x])
      print("----End Of Report----")
      print()

n = 10
e = Employee()
while n != 3:
  print("Main Menu")
  print("1. Add an Employee")
  print("2. Display all employee")
  print("3. Exit")
  print()
  temp = int(input("Enter you're response:"))
  n = temp
  if temp == 1:
    ID = input("Enter Employee ID:")
    Name = input("Enter Employee Name:")
    Age = input("Enter Employee Age:")
    Salary = input("Enter Employee Salary:")
    e.add_emp(ID,Name,Age,Salary)
  
  elif temp == 2:
    e.display_emp()
  
  else:
    print("Exiting The System")