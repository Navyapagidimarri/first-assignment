#we maximum used object is string for all
#we declare a string with ""

#i="navya"
#j='navya'
#print(i)
#print(j)

#here one thing is to confirm here is we can write a string with '' also

#slicing
#i="am working in marolix company"
#print(i[:15])
#print(i[4:10:-1])
#print(i[:])


#indexing
#i="am working in marolix company"
#print(i[10])




#concatenaton
#Example1
#i="navya"
#j=" working"
#k=" marolix"
#print(i+j+k)


#repetation with space at ening we can get perfect output
#i="navya "
#print(i*4)




#length of string by inbuilt function len()
#s="navya working in marolix"
#len_string=len(s)
#print(len_string)



#lenghth of the string by while loop
#i=0
#while(i<(len(s))):
 #   print(s[i],end="")
  #  i=i+1


#string reversal method
#s="navya working in marolix"
#n=""
#for i in s:
 #  n= i + n
#print(n)


#membership checking ----Boolean values are printing
#s="navya working in marolix"
#print("navya" in s)



#string sub string
# s=input("enter string:")
# s2=input("enter sub string:")
# if s not in s2:
#  print("yes")
# else:
#  print("not matching")



 #find
#s="navya working in marolix"
#print(s.find("a"))#it take 2nd a here
#print(s.find("a",17,22))#if we want selected variable then we have to declare start and end index
#print(len(s))#we are selecting reverse fun here
#print(s.rfind("i"))


#s="navya working in marolix"
#print(s.count("a"))#here we can count the variiable printing time



#comparing strings
# s="navya working in marolix"
# s2="harika working in marolix"
# if s>=s2:
#  print("s greaterthan s2")
# else:
#  print("s lessthan s2")#by ASCII values



#replacing string 
#s="navya working on python"
#s1="java"
#s1=s.replace("python",s1)
#print(s1)


#splitting string
# s="navya the working on the python"
# print(s.split("the"))


#remove item
#julymem=["navya","anusha","rushika","gayatri","bagwan","srinivas"]
#print(julymem.remove("navya"))
#print(julymem)


#polindrome
#s=input("enter polindrome:")
#if(s==s[::-1]):
#   print("yes it is polindrome")
#else:
#  print("No it is polindrome")


#vowel consonant
#s1=input("enter single alphabet:")


#if s1 in ("a","e","i","o","u","A","E","I","O","U"):
#   print("the entered alphabet is vowel")
#else:
#   print("the entered alphabet is consonant")


#s1=input("enter string1:")
#s2=input("enter string2:")
#anagrams must be in same length and with no order preference 
#if len(s1)!=len(s2):
#   print("not angrams")
#else:
# if sorted(s1)==sorted(s2):
#  print("both strings are  anagrams")
# else:
#   print("both strings are not  anagrams")




#sort the elements
#s=input("input alpahabets:")
#alphabets=[]
#digits=[]
#for k in s:
#   if s.isalpha():
#    alphabets.append(k)
#   else:
#       digits.append(k)
#output=''.join(sorted(alphabets)+sorted(digits))
#print(output)




#count occurance
#string="am happy to workng wiith marolix"
#s=string.count("a")
#print(s)



#count alphabets ,digits and special
#s="aabbcc121122@@"
#digitC=0
#alphaC=0
#specialC=0
#for i in s:
#   if i.isdigit():
#     digitC=digitC+1
#    elif i.isalpha(): 
#    alphaC=alphaC+1
#   else:
#    specialC=specialC+1
#print("number of special charactors",specialC)
#print("number of digit",digitC)
#print("number of digit",alphaC)



#sum of integers
#str1 = input('Enter a string: ')
#sum=0
#for i in str1:
#  if i.isdigit(): 
#        sum=sum+int(i)
#print("sum=",sum)

#s=[10,20,30,40]
#print(sum(s))



#replace the value
#s="am working in marolix"
#s2=s.replace(" ","the")
#print(s2)



#repeated string
#n=input("Enter the string:")
#for x in n:
#   print(x*5)



#repeated remove
#mylist = ["navya", "latha", "vaniitha", "kamala", "navya","navya"]
#mylist = list(dict.fromkeys(mylist))
#print(mylist)







