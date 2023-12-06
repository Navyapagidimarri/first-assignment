# a=input("enter a website name:")
# existed_login={"navya":"password"}
# if a.endswith(".com"):
#     print("welcome")
# else:
#     print("enter valid name")
# if True:
#         b=input("enter alredy registerred username :")
#         c=input("enter alrwady rwgistered password : ")
#         for key,value in existed_login.items():
#          if b==key and c==value:
#             print("login successfully")

#          else:
#             print("enter valid deatils")





# s=[1,2,3,4,5,5,6,6,7,7]
# t=[]
# for i in s:
#     if i not in t:
#         t.append(i)
# print(t)



# s=["1","2","3","4","5"]
# count=0
# for i in s:
#     count=count+int(i)
# print(count)


# l=[9,8,7,3,4,5,6]
# t=popitem(l)
# print(t)


#Python program to check given character is vowel or consonant
# input_char=input("enter char")
# vowels=["A","E","I","O","U","a","e","o","u"]
# if input_char in vowels:
#     print("given charactor is vowel")
# else:
#     print("given charactoe is consonant")



#count vowels
# input_sen=input("enter Input sentence :")
# vowels=["A","E","I","O","U","a","e","i","o","u"]
# count=0
# for i in input_sen:
#     if i in vowels:
#         count=count+1
# print(count)
  



#Python Program to count occurrence of a given characters in string.
# input_string="aaabb1234@@_"
# Aount=0
# ncount=0
# scount=0
# for i in input_string:
#     if i.isdigit():
#         ncount=ncount+1
    
#     elif  i.isalpha():
#         Aount=Aount+1
     
#     else:
#         scount=scount+1
      
# print("number count is",ncount)   
# print("alpha count is",Aount)
# print("special count is",scount)



#Python program to remove given character from String.
# input_string="am the new member"
# enter=" "
# for i in input_string:
#     input_string=input_string.replace("the",enter)
# print(input_string)



#Python Program to check if two Strings are Anagram.
# input_string1="navya"
# input_string2="avyan"
# if input_string1.isalpha() and input_string2.isalpha():
#     if len(input_string1)==len(input_string2):
#         if sorted(input_string1)==sorted(input_string2):
#             print("both are anagrams")
#         else:
#             print("both are not anagrams")

#     else:
#         print("lengths are not equal")
# else:
#     print("both are not alphabets")



#Python program to check a String is palindrome or not.
# input_string="navya"
# i=''.join(reversed(input_string))
# print(i)



#Python program to check given character is digit or not.
# input_string=input("enter a char")
# if input_string.isdigit():
#     print("given number is digit ")
# else:
#     print("given number is not integer")


#Python program to check given character is digit or not using isdigit() method.
# input_string=input("enter a char")
# print(type(input_string))



#Python program to replace the string space with a given character.
# input_string=input("enter")
# enter="merge"
# for i in input_string:
#     input_string=input_string.replace(" ",enter)
# print(input_string)


#Python program to convert lowercase char to uppercase of string.
# input_string="Am the NEW Member"
# new_string=""
# for i in input_string:
#     if  i.islower() and i.islower():
#      new_string=new_string+i.upper()
#     else:
#      new_string=new_string+i.lower()
# print(new_string)


#Python program to convert lowercase vowel to uppercase in string.
# input_string="Am the NEW Member"
# vowels=["a","e","i","o","u"]
# for i in input_string:
#   if i.lower() in vowels:
#     input_string=input_string.replace(i,i.upper())
# print(input_string)

#Python program to delete vowels in a given string.
# input_string=input("enter a word")
# input_deleted="A","E","I","o","u","a","e","i","o","u"
# for i in input_string:
#     if i in input_deleted:
#         input_string=input_string.replace(i,"")
# print(input_string)



#Python program to count the Occurrence Of Vowels & Consonants in a String.
# input1="aaaawwwwt"
# vowels="A","E","I","o","u","a","e","i","o","u"
# v_count =0
# c_count=0
# for i in input1:
#     if i in vowels:
#         v_count=v_count+1
#     else:
#         c_count=c_count+1
# print(v_count)
# print(c_count)


#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
# input1="aaeebbccdd123"
# vowels="A","E","I","o","u","a","e","i","o","u"
# for i in input1:
#     if i in vowels:
#          input1=input1.replace(i,"-",1)
#     break
# print(input1)


#Python program to concatenate two strings using join() method.
# n="navya"
# k="karthik"
# j="".join([n,k])
# print(j)


#Python program to check given character is digit or not.
# def trail(enter):
#  if enter.isdigit():
#     print("given charactor is a digit ")
#  else:
#     print("given charactor is  not digit ")
# enter=input("enter ")
# trail(enter)



#Python | Sort Python Dictionaries by Key or Value
# def trail(sorted):
#  dictionary={"navya":1,"anusha":2,"kavitha":3}
#  sorted_i=dict(sorted(dictionary.items()))
#  print(sorted_i)
# trail(sorted)



#Python program to find the sum of all items in a dictionary
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# sum=0
# for i in d.values():
#     sum=sum+i
# print(sum)



#Python program to find the size of a Dictionary
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# size=0
# for i in d.keys():
#     size=size+1
# print(size)



#Ways to sort list of dictionaries by values in Python – Using itemgetter
# from operator import itemgetter
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# get=itemgetter("navya")
# if get(d):
#     print("existed")
# else:
#     print("not existed")





# details={"navya":"abhi@1234"}
# key =input("enter username")
# value=input("enter password:")
# if key in details and value==  details[key ]:
#         print("successfully entered")
# else:
#         print("not valid")




# d={"navya":20000,"kavya":30000,"mamatha":40000}
# e={"kamala":50000,"vanitha":60000}
# f=d|e
# print(f)




#Python – Remove duplicate values across Dictionary Values
# d={"navya":20000,"kavya":30000,"mamatha":40000,"bhavya":20000}
# print(list(set(d.values())))



#Python | Ways to remove a key from dictionary
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# del d["navya"]
# print(d)


# d={"navya":20000,"kavya":30000,"mamatha":40000}
# print(d.popitem("navya"))



# d={"navya":20000,"kavya":30000,"mamatha":40000}
# print(d.clear())
# print(d)



#Python – Replace words from Dictionary
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# d["kavya"]=50000
# print(d)




#Python program to find the sum of all items in a dictionary
# d={"navya":20000,"kavya":30000,"mamatha":40000}
# count=0
# for i,j in d.items():
#     count=count+j
# print(count)



#Python – Replace words from Dictionary\
d={"navya":20000,"kavya":30000,"mamatha":40000}
for i,j in d.items():
    d["navya"]=30000
print(d)











