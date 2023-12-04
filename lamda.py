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




# l=[1,1,2,2,3,3]
# new_list =[]
# for i in l:
#    if i not in new_list:
#        new_list.append(i)
# print(new_list)


s="madam"
t=''.join(reversed(s))
if s == t:
    print("it is a  polindrome :")
else:
    print("its not polindrome")
    
