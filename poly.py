#sample practice odf polymarphism + operator
# a=2
# b=3
# print(a + b)
# print("py" + "thon")#here we are tried 2 diff example with + operator



# class principal:
#     def __init__(self,responcibilty):
#         self.responcibilty=responcibilty
#     def work(self):
#         print("Prinicial have to mange total school envirnonment")
# class teacher:
#     def __init__(self,responcibilty):
#         self.responcibilty=responcibilty
#     def work(self):
#         print("teacher have to manage all the students education")
# class student:
#     def __init__(self,responcibilty):
#         self.responcibilty=responcibilty
#     def work(self):
#         print("Student must have thwir home works")
# p=principal("managemnat")
# t=teacher("teaching")
# s=student("attendingschool")
# for i in [p,t,s]:
#     i.work()




#Operator overloading
# class magic:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,second):
#         return self.x +second.x
# m1=magic(10)
# m2=magic(20)
# print(m1+m2)



#method overloading
# class main:
#     def m1(self):
#         print("first method")
#     def m1(self):
#         print("second method")
# m=main()
# m.m1()



#consrtutor overloading
# class main:
#     def __init__(self):
#         print("this is the method -1")
#     def __init__(self):
#         print("this is the method -2")#final declaration constrctor only taken
# m=main()



#constructor overriding
class c1:
    def method1(self):
        print("its is a first class")
class c2(c1):
    def method1(self):
        print("its a second method")
c=c2()
c.method1()






