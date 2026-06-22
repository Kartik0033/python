import  random
# (add company name to employee)suppose we want to change company name according to logic of each employee then we cant change it  using 
# object for each emp so easy way is to create a class method which will be applicable for  all the objects in it  (using just one line call class method )
class Employee:

  companyname = "Google"

  def __init__(self,name,designation,age) -> None: #means return none
    self.name = name
    self.designation = designation
    self.age = age
    self.empid = self.generate_empid()

  def generate_empid(self):
    return (f"emp-{random.randint(1,100)}")

  def show_employee(self):
    print(f"""
  Empid : {self.empid}
  Name: {self.name}
  Designation: {self.designation}
  Age: {self.age}
  Company Name: {self.companyname}
  """)
    
  @classmethod
  def changecompany(cls):
    companies = ["Apple.inc","GOogle","Microsoft"]
    company = random.choice(companies)
    cls.companyname = company
    print("Company Changed")
    

Employee.changecompany()

emp1 = Employee("Kartik","PythonDeveloper",19)
# emp1.companyname = "apple"
#print(id(emp1.companyname))  # this shows that new company  name var is created in the object
#print(id(Employee.companyname))# this shows that only same value is  share but  wwhen changed the new variable is made in object insttance
emp1.show_employee()


emp2 = Employee("Shree","JavDeveloper",20)
emp2.show_employee()
    
emp3 = Employee("Josh","Product Manager",20)
emp3.show_employee()
    