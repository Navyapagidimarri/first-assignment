# a=100
# def my_function():
#     a=10
#     print(a)
# my_function()#it takes inside varible "a" That is because of its local function'



# a=100
# def my_function():
#     b=200
#     print(a+b)#variabbles are different so it take out side of the function 
# my_function()



# a=int(input("enter table number"))#global variable
# def table_function():
#     table_count=1
#     while(table_count<11):
#         table_count=table_count+1
#         print(a ,"X",table_count ,"=",a*table_count)
# table_function()



# sahithi_school_data="1st class"
# d={}
# def student_data():
#     for i in range(0,2):
#         name=input("enter name:"+str(i)+":")
#         id=input("enter id:"+str(i)+":")
#         d[name]=id
#         print(sahithi_school_data,":",d)
# student_data()




#counting milk 
# customer_details=eval(input("number of customers:"))
# def counting_milk():
#     l={}
#     for i in range(0,customer_details):
#       global counting_milk():
#       name=input("enter customer name:")
#       milk_rate=int(input("enter rate :"))
#       number_of_leters=int(input("enter number of leters"))
#       count=milk_rate*number_of_leters
#       l[name]=count
#       print(l)
#       total_count=sum(l.values())
#       print(total_count)
# counting_milk()



#@ variables checking blobal declaration
# s="tagore international school"
# def global_example():
#   s="uniq english medium high school"
#   student_name=input("Enter Student name:")
#   print(student_name ,"studying in",s)
# global_example()
# def global_exmple2():
#     global s
#     student_name1=input("Enter Student name:")
#     print(student_name1,"studying in",s)
# global_exmple2()



# def sum_function():
#     l=[8,2,3,0,7]
#     sum(l)
#     result=sum(l)
#     print(result)
# sum_function()




def factorial(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return factorial(n - 1) + factorial(n - 2)
num=8
my_result=factorial(num)
print(my_result)



    










