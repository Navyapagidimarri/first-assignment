#represents in {}
#s={"a","b","c"}
#print(s)
#its not follow the order
#dont follow the slicing and indexing



# s={1,2,3,4}
# l=[5,6,7,8]
# s.update(l)
# print(s)



#here one project about student names:adding
# s=eval(input("enter string values"))
# s1=set()
# for x in range(0,s):
#     y=input("elements:"+str(x)+":")
#     s1.add(y)
# print(s1)




# s={1,2,3,4}
# s.clear()
# print(s)


# s1={1,2,3,4}
# s2={3,4,5,6}
# s3=s1.symmetric_difference(s2)
# print(s3)



# s1={1,2,3,4}
# s2={3,4,5,6}
# s3=s1.difference(s2)
# print(s3)

#intersection
# s1=eval(input("enter elements range"))
# s2=eval(input("eenter elements range"))
# s3=set()
# s4=set()
# for x in range(0,s1):
#     item=input("enter elements:"+str(x)+":")
#     s3.add(item)
# for y in range(0,s2):
#     item=input("enter elements:"+str(y)+":")
#     s4.add(item)
# s5=s3.intersection(s4)
# print(s5)


# symmetric
# s1=eval(input("enter elements range"))
# s2=eval(input("eenter elements range"))
# s3=set()
# s4=set()
# for x in range(0,s1):
#   item=input("enter elements:"+str(x)+":")
#   s3.add(item)
# for y in range(0,s2):
#     item=input("enter elements:"+str(y)+":")
#     s4.add(item)
# s5=s3.symmetric_difference(s4)
# print(s5)



s1=eval(input("enter elements range"))
s2=eval(input("eenter elements range"))
s3=set()
s4=set()
for x in range(0,s1):
  item=input("enter elements:"+str(x)+":")
  s3.add(item)
for y in range(0,s2):
    item=input("enter elements:"+str(y)+":")
    s4.add(item)
s5=s3.difference(s4)
print(s5)


