# class parent:
#     def __init__(self):
#         print("this is sample super class")
# class child(parent):
#     def __init__(self):
#      super().__init__()
#      print("this is base class")
# c=child()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname,lname,year):
#         super().__init__(fname, lname)
#         self.year = year  # Use the passed 'year' parameter

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.year)

# s = Student("navya", "pagidimarri", 2019)
# s.printname()
# s.welcome()  




# class principal:
#       fee=50000
#       def __init__(self):
#             print("PRINICIPALL TO PARENT :please clear school fee immediatly")
# class teacher(principal):
#       def __init__(self):
#         super().__init__()
#         print("TEACHER TO PARENTS :please check homework dairy  everyday")
# o1=teacher()


class lalthajewellery:
  def __init__(self,chains,bangles):
    self.chains=chains
    self.bangles=bangles
  def kuktaplly(self):
    print("in kuktapally branch avaiable chains starting weight is:",self.chains)
    print("in kuktapally branch avaiable bangles strarting weight is",self.bangles)
class dilsuknagar(lalthajewellery):
 def __init__(self,chains,bangles,jumkas,rings):
  super().__init__(chains,bangles)
  self.jumkas=jumkas
  self.rings=rings
 def dil(self):
  super().kuktaplly()
  print("in dilusknagar branch available jumkas starting weight is :",self.jumkas)
  print("in dilusknagar branch available rings starting weight is : ", self.rings)
c=dilsuknagar("10grms","20grams","2grams","1grms")
c.dil()




#Sample variables accessing with self
# class base:
#   a=50
#   def __init__(self):
#     self.b=30
# class derived(base):
#   def __init__(self):
#    super().__init__()
#    self.c=40
#    print(super().a + self.b +self.c )
# c=derived()



# class data:
#   def __init__(self,name,domain):
#     self.name=name
#     self.domain=domain
#   def m1(self):
#     print("name:",self.name)
#     print("age:",self.domain)
#   @staticmethod
#   def m3():
#     print("this is the static method")  
# class entry(data):
#   @classmethod
#   def m2(cls):
#     super(data,cls).__init__(cls)#here we can access constructor 
#     cls.address="kondapur"
#     cls.office="marolix technology"
#     print("address:",cls.address)
#     print("designation",cls.office)
#   @staticmethod
# c=entry("navya","python" )
# c.m1()
# c.m2()






