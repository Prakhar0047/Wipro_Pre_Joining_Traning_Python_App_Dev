class Employee:    
  emp_list = {}
  def __init__ (self,emp_no, emp_name, salary):    
    self.emp_no = emp_no
    self.emp_name = emp_name
    self.salary = salary

  def create_new_emp(self,emp_no):
    self.emp_list[emp_no] = [self.emp_name,self.salary]
  
  def Delete_emp(self,emp_no):
    self.emp_list.pop(emp_no)
  
  def display_emp(self,emp_no):
    details = self.emp_list[emp_no]
    print("Employee Number:",emp_no)
    print("Employee Name:",details[0])
    print("Employee Salary:",details[1])

  def max_salary(self):
    max_sal = 0
    e_num = 0
    for x in self.emp_list:
      details = self.emp_list[x]
      if details[1] > max_sal:
        max_sal = details[1]
        e_num = x
    self.display_emp(e_num)
    
# Driver Code
emp1 = Employee(1,"Prakhar",120000)
emp2 = Employee(2,"Shivam",110000)
emp3 = Employee(3,"Upinder",100000)

emp1.create_new_emp(1)
emp2.create_new_emp(2)
emp3.create_new_emp(3)

emp1.display_emp(1)
del emp3
emp1.max_salary()