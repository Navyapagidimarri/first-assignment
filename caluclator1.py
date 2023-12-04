class cal:
    def __init__(self):
        self.num1=int(input("enter number"))
        self.num2=int(input("enter number"))
    def add(self):
        self.addition=self.num1+self.num2
        print(self.addition)
    def mul(self):
        self.multiplication=self.num1*self.num2
        print(self.multiplication)
    def sub(self):
        self.substraction=self.num1-self.num2
        print(self.substraction)
    def div(self):
        self.division=self.num1/self.num2
        print(self.division)
    def process(self):
        while True:
            print("select operation :")
            print("Addition -1")
            print("substraction -2")
            print("multiplication - 3")
            print("division -4")
            print("exit-5")
            section=input("enter choice 1/2/3/4/5")
            if section in  ["1","2","3","4","5"]:
                if section=="1":
                    self.add()
                if section=="2":
                    self.sub()
                if section=="3":
                    self.mul()
                if section=="4":
                    self.div()
                if section=="5":
                    break
object=cal()                    
object.process()




# class cal:
#     def __init__(self):
#         self.num1=int(input("enter number"))
#         self.num2=int(input("enter number"))
#     def add(self):
#         self.addition=self.num1+self.num2
#         print(self.addition)
#     def mul(self):
#         self.multiplication=self.num1*self.num2
#         print(self.multiplication)
#     def sub(self):
#         self.substraction=self.num1-self.num2
#         print(self.substraction)
#     def div(self):
#         self.division=self.num1/self.num2
#         print(self.division)

#     def process(self):
#         while True:
#             print("select operation :")
#             print("Addition -1")
#             print("substraction -2")
#             print("multiplication - 3")
#             print("division -4")
#             print("exit-5")
#             section=input("enter")
#             if section in  ["1","2","3","4","5"]:
#                 if section=="1":
#                     object.add()
#                 elif section=="2":
#                     object.mul()
#                 elif section=="3":
#                     object.sub()
#                 elif section=="4":
#                     object.div()
#                 elif section=="5":

#                     break
# object=cal()
# object.process()