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
#s=input("enter string:")
#s2=input("enter sub string:")
#if s not in s2:
 # print("yes")
#else:
 # print("not matching")

 #find
#s="navya working in marolix"
#print(s.find("a"))#it take 2nd a here
#print(s.find("a",17,22))#if we want selected variable then we have to declare start and end index
#print(len(s))#we are selecting reverse fun here
#print(s.rfind("i"))

#s="navya working in marolix"
#print(s.count("a"))#here we can count the variiable printing time

#comparing strings
s="navya working in marolix"
s2="harika working in marolix"
if s>=s2:
  print("s greaterthan s2")
else:
  print("s lessthan s2")#by ASCII values


#replacing string 
s="navya working on python"
s1="java"
s1=s.replace("python",s1)
print(s1)







