# class Sample:#variable name
#     print("this is my class")
#     def display(self):
#         a=10
#         b=20
#         print(a,b)
# obj=Sample()
# obj.display()



# class fruits:
#     print("here so many fruits are there")
#     def __init__(self,name,colour,taste):
#         self.name=name
#         self.colour=colour
#         self.taste=taste
#     def display(self):
#         print("name:",self.name)
#         print("colour:",self.colour)
#         print("taste:",self.taste)
#         print("----------------------------")
# obj=fruits("apple","red","sweet")
# obj.display()
# obj1=fruits("orange","orange","sour")
# obj1.display()





# class register:
#     def __init__(self,name,password,email):
#         self.name=name
#         self.password=password
#         self.email=email
#     def display(self):
#         print("login:",self.name)
#         print("password",self.password)
#         print("email:",self.email)
#         print("-----------------")
# entry=int(input("enter number of customers"))
# for i in range(entry):
#  input_name=input("enter name")
#  input_password=input("enter password")
#  input_email=input("enter email")
#  obj = register(name=input_name, password=input_password, email=input_email)
#  obj.display()



# class employee:
#     def __init__(self,name,salary,id):
#         self.name=input_name
#         self.id=input_id
#         self.salary=input_salary
# marolix_entry=int(input("enter employee details"))
# e={}
# for entry in range(marolix_entry):
#  input_name=input("enter employee name:")
#  input_id=input("enter id:")
#  input_salary=input("enter salary:")
#  e[input_name]=employee(input_name,input_id,input_salary)
#  print(e[input_name].__dict__)




class Employee:
    company="marolix Technology solutions"
    def __init__(self,name,salary,mobile_number):
        self.name=name
        self.salary=salary
        self.mobile_number=mobile_number
    def domain(self):
        Employee.domain="java"
        self.domain="python"
        self.company="zenpact technologies"
        print("method level static variable: " ,self.company)
    @classmethod
    def id(cls):
        Employee.id=1689
        cls.company="tech mahendra"
        print("class mthod level variable: " ,Employee.company)
    @staticmethod
    def place():
        Employee.place="kondapur"
        Employee.company="kclink technology solutions"
        print("static level variable:" , Employee.company)
e1=Employee("navya",15000,9876543210)
print("class level static variable:",Employee.company)#class level company name displayed -marolix
e1.domain()#domain level company name dsiplayed -zenpact 
e1.id()#class level comapny tech mahendra declared - tech mahendra
e1.place()#static level company name dsiplayed kclink
print(e1.__dict__)
print(Employee.__dict__)
