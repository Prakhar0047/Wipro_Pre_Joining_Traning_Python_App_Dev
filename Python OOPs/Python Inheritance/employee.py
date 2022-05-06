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
    print(self.emp_list[emp_no])

  def max_salary(self):
    max_sal = 0
    e_num = 0
    for x in self.emp_list:
      details = self.emp_list[x]
      if details[1] > max_sal:
        max_sal = details[1]
        e_num = x
    self.display_emp(e_num)