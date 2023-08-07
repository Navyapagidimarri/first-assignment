s1=input("enter string1:")
s2=input("enter string2:")
#anagrams must be in same length and with no order preference 
if len(s1)!=len(s2):
   print("not angrams")
else:
  if sorted(s1)==sorted(s2):
   print("both strings are  anagrams")
  else:
    print("both strings are not  anagrams")