import random
import employee

class job(employee.Employee):
  job_salary = {}
  def __init__(self, emp_no, emp_name, job, losal, hisal):
    self.emp_no = emp_no
    self.emp_name = emp_name
    self.job = job
    self.losal = losal
    self.hisal = hisal
  
  def salary_calculator(self,job):
    salary = random.randint(self.losal, self.hisal)
    self.job_salary[job] = salary

  def create_new_emp(self):
    self.emp_list[self.emp_no] = [self.emp_name,self.job,self.job_salary[self.job]]
    
# Driver Code
# Object -> E_no, E_name, losal, hisal
j = job(1,"Prakhar","SDE",1200000,1400000)
j2 = job(2,"Prakhar","SDE",1200000,1400000)
j.salary_calculator("SDE")
j.create_new_emp()
j.display_emp(1)
j2.create_new_emp()
j2.display_emp(2)