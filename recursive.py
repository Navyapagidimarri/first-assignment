#recursive method nothing but one funtion will call itself again and again
# def factorial_function(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial_function(x-1))
# num=4
# answer=factorial_function(num)
# print(answer)



#1.Write a Python program to calculate the sum of  numbers.
# def sum_function(x):
#     if x==1:
#         return 1
#     else:
#         return x+sum_function(x-1)
# num=5
# answer=sum_function(num)
# print(answer)



#2.write a fabonacii series
# def febonaci_series(n):
#     if n==0 or n==1:
#         return 1
#     else:
#          return febonaci_series(n-1)+febonaci_series(n-2)
# answer=febonaci_series(10)
# print(answer)



#3.write a patterndef print pattern
# 'def pattern_recursion(n):
#     if n > 0:
#         print("* " * n)
#         pattern_recursion(n - 1)

# pattern_recursion(5)

#filter capitals
# def capital_letter(str):
#     return str.isupper()
# s = "Navya WORKING in Marolix"
# filtered_capitals = filter(capital_letter, s)
# output = ''.join(filtered_capitals)
# print(output)



# '#divisable by 4
# def divisible(n):
#     s=eval(input("enter elements:"))
#     l=[]
#     for i in range(0,s):
#         if i%4==0:
#           element=input("enter elemnetnt:",+str(i),":")
#           l.append(element)
#           print(l)
#         else:
#          return none
# # divisible = filter(divisible,i)
# # print (list(divisible))'



#calulating power 
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base=2
exponent=5
output=power(base,exponent)
print(output)



