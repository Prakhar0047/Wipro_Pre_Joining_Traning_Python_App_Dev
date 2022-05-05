import random
import employee

class job(employee.Employee):
  salary = 0

  def __init__(self,job,losal,hisal):
    self.job = job
    self.losal = losal
    self.hisal = hisal
  
  def job_salary(self):
    self.salary = random.randint(self.losal, self.hisal)

  def create_new_emp(self,emp_no,emp_name):
    self.emp_list[emp_no] = [emp_name,self.salary]
    

j = job("SDE",100000,120000)
j.job_salary()
j.create_new_emp(1,"Shivam")
j.display_emp(1)