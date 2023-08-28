# def example(a,b):
#     print(a+b)
# a=20
# b=30
# example(a,b)




#printing odd numbers by def function
# def oddnumbers(x,y):
#     l=[]
#     for i in range(x,y):
#         i%2 !=0
#         l.append(i)
#         print(i)
# oddnumbers(0,50)
# oddnumbers(0,100)
# oddnumbers(0,150)




# def greet(name):
#     print("helloo"+name)
# greet("navya")
# greet("marolix")




#count area of a square
# def squareornot(length,breadth):
# #for sqaure lenth and breadth is same otherwise it's not square
#     if length==breadth:
#         print("this is a sqaure")
#     else:
#         print("no this is not a square")
# squareornot(20,20)
# squareornot(30,20)




#polindrome
# def polindromeornot(x):
#     if (x[::-1]==x):
#         print("it's polindrome")
#     else:
#         print("it's not polindrome")
# polindromeornot("madam")
# polindromeornot("navya")




#count 
def countelements(s):
  digitC=0
alphaC=0
specialC=0
for i in s:
  if i.isdigit():
    digitC=digitC+1
  elif i.isalpha(): 
   alphaC=alphaC+1
  else:
   specialC=specialC+1
print("number of special charactors",specialC)
print("number of digit",digitC)
print("number of digit",alphaC)
countelements("navya0112233@!")





     

