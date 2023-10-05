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




class register:
    def __init__(self,name,password,email):
        self.name=name
        self.password=password
        self.email=email
    def display(self):
        print("login:",self.name)
        print("password",self.password)
        print("email:",self.email)
        print("-----------------")
entry=int(input("enter number of customers"))
for i in range(entry):
 input_name=input("enter name")
 input_password=input("enter password")
 input_email=input("enter email")
 obj = register(name=input_name, password=input_password, email=input_email)
 obj.display()




