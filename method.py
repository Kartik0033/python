
class A :
  def f1(self): #instance method both f1 and f2
    print("Hello World")

  def f2(self,a,b):
    self.a = a
    self.b = b
    print("value of a ",a,"value of b",b)

obj1 = A() #instance object
obj1.f1() #implicilty pass the self obj1 to self  obj which is mandatory to create.
obj1.f2(4,5)
A.f1(obj1)  #can also call using the class object but need to pass obj to the self
A.f2(obj1,6,7)

class B:
  @staticmethod
  def f1():
    print("Hello WOrld")
  
  @staticmethod
  def f2(a,b):
    a = a
    b = b
    print("value of a ",a,"value of b",b)
    print()

B.f1()
B.f2(5,10)
obj1=B()
obj1.f1() #static method call using instance
obj1.f2(4,5)
