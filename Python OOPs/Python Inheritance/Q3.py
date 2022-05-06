import employee
from datetime import date as date_n
class contract_employee(employee.Employee):
  def __init__(self,start_date,end_date):
    self.start_date = start_date
    self.end_date = end_date
    self.date_str = str(self.no_of_days)
    self.date_list = self.date_str.split()

  def salary(self,per_day):
    print("You're Salary is:",int(self.date_list[0])*per_day)

e1 = employee.Employee(1,"Prakhar",120000)
e2 = employee.Employee(2,"Shivam",110000)
e3 = employee.Employee(3,"Upinder",100000)

e1.create_new_emp(1)
e2.create_new_emp(2)
e3.create_new_emp(3)

s_yy = int(input("Enter Starting Year"))
e_yy = int(input("Enter Ending Year"))
s_mm = int(input("Enter Starting Month"))
e_mm = int(input("Enter Ending Month"))
s_dd = int(input("Enter Starting Day"))
e_dd = int(input("Enter Ending Day"))

Start_date = date_n(s_yy, s_mm, s_dd)
End_date = date_n(e_yy, e_mm, e_dd)

ce1 = contract_employee(Start_date, End_date)
ce1.salary(10)