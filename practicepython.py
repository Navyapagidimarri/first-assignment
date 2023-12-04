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


#Python – Sum of tuple elements
# def tuple(n):
#     tuple_sum=sum(n)
#     print(tuple_sum)
# n=(10,20,30,40)
# tuple(n)



# def tuple(n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# n=(10,20,30,40)
# tuple(n)

        

#Remove items from Set
# def sett(n):
#  n_copy = n.copy()
#  for i in n_copy:
#         n.remove(i)
#         print(i)
# n={1,2,3,4,5}
# sett(n)
# print(n)



#factorial
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         factorial=n*fact(n-1)
#         return  factorial
# number=int(input("enter number :"))
# result=fact(number)
# print(f"The factorial of {number} is: {result}")



l = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7]
count_dict = {}
for i in l:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
max_frequency = max(count_dict.values())
max_elements = [key for key, value in count_dict.items() if value == max_frequency]
print(f"The maximum frequency is: {max_frequency}")
print(f"The element(s) with the maximum frequency is/are: {max_elements}")




# s="Am navya"
# s1=""
# for i in s:
#     if i.isupper():
#         i=i.lower()
#     s1=s1+i
# print(s1)



# s=eval(input("enter word"))
# i=eval(input("enter index number :"))
# j=eval(input("enter second index number :"))
# if len(s)>=2:
#     s=list(s)
#     s[i] ,s[j] = s[j],s[i]
#     swappedstring=''.join(s)
#     print(swappedstring)





# def add(n):
#     count=0
#     for i in n:
#         count+=i
#     return count
# n=[1,2,3,4,5]
# result=add(n)
# print(result)


# def add(n):
#     print(sum(n))
# n=[1,2,3,4,5]
# add(n)


# vowels=["A","E","I","O","U","a","e","i","o","u"]
# n="navya working in marolix"
# for vowel in vowels:
#    n= n.replace(vowel,'')
# print(n)



# n="navya working in marolix"
# for i in n:
#     if n.islower():
#         v=n.upper()
# print(v)



#Write a program in Python to find sum of digits of a number using recursion?
# def test(n):
#     if len(n)==0:
#      return 0
#     else:
#         count=n[0]+test(n[1:])
#     return count
# n=[1,2,3,4,5]
# result=test(n)
# print(result)



# def panagram(n):
#     k=set(n)
#     if k.isalpha():
#         new=k.lower()
#     print(new)
#     if len(k)==26:
#         print("it is anagram")
#     else:
#         print("it is not an angram")
    
# n="navyaworkingin"
# panagram(n)


# from functools import reduce
# l=[1,2,3,4,5]
# new=reduce(lambda x,y:x**y,l)
# print(new)



#Convert Integer Matrix to String Matrix
S=[[1,2,3],[4,5,6],[7,8,9]]
t=[]
for i in S:
    k=list(map(str,i))
    print(k)
    


     
 
   
        



