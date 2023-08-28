#1.Write a Python script to add a key to a dictionary.
# d={}
# for k in range(0,5):
#     key=input("enter keys:")
#     value=input("enter values:")
#     d[key]=value
# print(d)
# update_key=input("enter update key")
# update_value=input("enterupdate keys")
# d.update({update_key:update_value})
# print(d)


## 2..Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# #Sample Dictionary
# #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# d1=dict()
# for x in range(1,16):
#     d1[x]=x**2
# print(d1)  



#3.Write a Python program to iterate over dictionaries using for loops
# d={}
# for k in range(0,5):
#     key=input("enter keys")
#     value=input("enter values")
#     d[key]=value
# print(d)




#4.Write a Python program to remove a key from a dictionary.
# d={}
# for k in range(0,5):
#     key=input("enter keys:")
#     value=input("enter values:")
#     d[key]=value
# print(d)
# remove_key=input("enter removed key")
# d.pop(remove_key)
# print(d)



#5.Write a Python program to access dictionary key's element by index.
# d={}
# for k in range(0,5):
#     key=input("enter keys:")
#     value=input("enter values:")
#     d[key]=value
# print(d)
# print(list(d)[0])#converted into list
# print(list(d)[1])
# print(list(d)[2])



#6.Write a Python script to check whether a given key already exists in a dictionary.
# d={}
# for k in range(0,5):
#     key=input("enter keys:")
#     value=input("enter values:")
#     d[key]=value
# print(d)
# enter_key=input("enter a key")
# enter_value=input("enter a value")
# if enter_key in d.keys():
#     print("key already exists")
# else:
#     d.update({enter_key:enter_value})
# print(d)




#7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for key ,value in d1.items():
#         if key in d2:
#             d2[key]=d1[key]+d2[key]
#         else:
#             d2[key]=d1[key]
# print(d2)

#8.Write a Python script to merge two Python dictionaries.
# d={}
# d2={}
# d3={}
# for k in range(0,2):
#     key_1=input("enter keys:"+str(k)+":")
#     value_1=input("enter values:"+str(k)+":")
#     key_2=input("enter keys:")
#     value_2=input("enter values:")
#     d[key_1]=value_1
#     d2[key_2]=value_2
# print(d)
# print(d2)
# d3= d | d2#merge operator
# print(d3)


#9.Write a Python program to sum all the items in a dictionary.
# d={"navya":20000,"kavitha":30000,"sunitha":40000}
# print(sum(d.values()))


#10.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
str = "marolix technology"
dict ={}
for s in str:
   dict[s]=str.count(s)
print(dict)