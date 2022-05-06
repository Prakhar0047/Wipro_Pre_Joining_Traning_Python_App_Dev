import employee
class bonus(employee.Employee):
  def __init__(self,bonus):
    self.bonus = bonus

  def salary_update(self):
    for x in self.emp_list:
      det = self.emp_list[x]
      det[1]+=self.bonus

e1 = employee.Employee(1,"Prakhar",120000)
e2 = employee.Employee(2,"Shivam",110000)
e3 = employee.Employee(3,"Upinder",100000)

e1.create_new_emp(1)
e2.create_new_emp(2)
e3.create_new_emp(3)

b = bonus(50000)
b.salary_update()
print(b.emp_list)