#.Write a Python script to add a key to a dictionary.
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
d={}
for k in range(0,5):
    key=input("enter keys:")
    value=input("enter values:")
    d[key]=value
print(d)
remove_key=input("enter removed key")
d.pop(remove_key)
print(d)

