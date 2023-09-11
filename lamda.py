# def lambda_function1(n):
#   return lambda a : a * n
# double_value = lambda_function1(2)
# print(double_value(10))



#power 
# def lambda_function2(n):
#   return lambda x:x**n
# power=lambda_function2(2)
# print(power(10))


# def lambda_function3():
#   l=[10,20,30,40,50]
#   k=[]
#   k.extend(filter(lambda  i: i % 4 == 0, l))
#   return k
# result = lambda_function3()
# print(result)



def lambda_function4():
    l = []
    input_string = input("Enter elements separated by spaces: ")
    elements = input_string.split()  
    l.extend(filter(lambda i: int(i) % 4 == 0, elements))
    return l
result = lambda_function4()