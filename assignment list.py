#write a prog to merge two lists
# l=[10,"navya","telangana"]
# t=(20,"anusha","andhrapradesh")#tuple
# l.extend(t)
# print(l)


#sum of 2 lists
# l1=eval(input("enter the size1:" ))
# l2=eval(input("enter the size2:"))
# new_list1=[]
# new_list2=[]
# sum_list=[]
# for i in range(0,l1):
#    element1=int(input("enter the element:"+str(i)+":"))
#    new_list1.append(element1)
# print(new_list1)
# for i in range(0,l2):
#   element2=int(input("enter the element:"+str(i)+":"))
#   new_list2.append(element2)
# print(new_list2)
# for i in range(len(new_list2)):
#   sum_list.append(new_list1[i]+new_list2[i])
# print(sum_list)



#find even number
# l=eval(input("enter number"))
# empty_list=[]
# for i in l:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

#find odd number
# l=eval(input("enter number:"))
# empty_list=[]
# for i in l:
#     if i%2 != 0:
#         empty_list.append(i)
# print(empty_list)


# #del element of given index
# l=[10,"navya",12.41,True,9+9j]
# del(l[0])#10 wiill be removed
# print(l)


#del element directly
# l=[10,"navya",12.41,True,9+9j]
# l.pop()
# print(l)


#insert element at the specified index
# l=[10,20,40,50,60,70]
# l.insert(2,30)
# print(l)


#insert element at the end
# l=[]
# l.append("latha")
# l.append("seetha")
# l.append("anitha")
# l.append("sunitha")
# l.append("vanitha")
# print(l)


#size of the list5

l1=eval(input("enter the size1:" ))
l2=eval(input("enter the size2:"))
new_list1=[]
new_list2=[]
for i in range(0,l1):
   element1=int(input("enter the element:"+str(i)+":"))
   new_list1.append(element1)
print(new_list1)
for i in range(0,l2):
  element2=int(input("enter the element:"+str(i)+":"))
  new_list2.append(element2)
print(new_list2)
if len(new_list1)==len(new_list2):
    print("length are equal")
else:
    print("length are not equal")