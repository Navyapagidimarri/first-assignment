#1)Python program to interchange first and last elements in a list
# input1=eval(input("enter elements"))
# print("first entered list ",input1)
# if len(input1)>=2:
#      input1[0] , input1[-1]=input1[-1],input1[0]
# print("second entered list ",input1)   


#Maximum of two numbers in Python
# def maxnumber(a,b):
#      print(max(a,b))
# maxnumber(10,20)



#Minimum of two numbers in Python
# def minnumber(a,b):
#      print(min(a,b))
# minnumber(10,20)



#Python | Ways to find length of list -
# def length(i):
#  print(len(i))
# i=eval(input("enter elemnts :"))
# length(i)



#Python program to swap two elements in a list
# def swap(l,i,j):
#     print("1st list ",l)#it should be in list only
#     print("length of list ",len(l))
#     if len(l)>=2:
#       l[i],l[j] =l[j] ,l[i]
#     print("swapped list ",l)
# l=eval(input("enter elements :"))
# i=int(input("ente index in perfect range"))
# j=int(input("ente index in perfect range"))
# swap(l,i,j)


#Python program to check whether the string is Symmetrical or Palindrome
# def polindrome(n):
#     if n ==n[::-1]:
#         print("its is polindrome :")
#     else:
#         print("Given String is not polindrome")
# n=input("Enter String in String format only")
# polindrome(n)


# Reverse words in a given String in Python
# def rev(n):
#     print(n[::-1])
# n=input("enter string")
# rev(n)


# Ways to remove i’th character from string in Python
# def rem(n,i):
#     print("entered string is" ,n)
#     new_string=list(n)
#     del new_string[i]
#     final_string=''.join(new_string)
#     print(final_string)
# n=input("enter String:")
# i=int(input("enter index "))
# rem(n,i)




# Find length of a string in python (2 ways)
# def word(n):
#     print(len(n))
# n=input("enter string")
# word(n)
#method2
# def word(n):
#     count=0
#     for i in n:
#         if i in n:
#          count+=1
#     print(count)
# n=input("enter string")
# word(n)




# Python program to print even length words in a string
# def even_words(n):
#     new_string=n.split(' ')
#     print(new_string)
#     for i in new_string:
#        if  (len(i))%2==0:
#         print(i)
# n=input("enter word : ")
# even_words(n)


#typecas
# a=101
# print(a)


# a=int(786.4)
# print(a)
#here am using float value assigned to interger it leaves after decimal it prints only before decimal value



#b=int(True)
#print(b)
#here am using boolean vale to int then it gives 1 for true and 0 for false automatically


# c=int(1+3j)
# print(c)
#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


# c=int("marolix")
# print(c)
#ValueError: invalid literal for int() with base 10: 'marolix'


#Write a program in Python to check whether an integer is Armstrong number or not.
# def armstrong(abc):
#  number=str(abc)
#  length=len(number)
#  sum_of_digits=0
#  for i in number:
#     sum_of_digits=int(i)**3+sum_of_digits
#  if abc == sum_of_digits:
#         print("this is armstrong number :")
#  else:
#         print("this is not armstrong number")
# armstrong(153)


# create a table with while loop and for loop
# l=int(input("enter table name"))
# i=1
# while(i<11):
#     print(l,'X',i ,'=',l*i)
#     i=i+1


#Python Program to check a given number is even or odd.
# def even_odd(n):
#     for i in n:
#         if i % 2 == 0:
#             print(f"{i} is an even number.")
#         else:
#             print(f"{i} is an odd number.")

# n = [1, 2, 3, 4, 5, 6, 7, 8]
# even_odd(n)




#write a Python program to calculate the sum of  numbers.
# def sum_function(x):
#     if x==1:
#         return 1
#     else:
#         return x+sum_function(x-1)
# num=5
# answer=sum_function(num)
# print(answer)



#write a prog to find sqaure 
# def square(base,exponent):
#     result=base**exponent
#     if exponent ==0:
#         print (base)
#     else:
#       print(result)
# square(2,3)


