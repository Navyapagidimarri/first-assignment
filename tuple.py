#declaration of tuple
# i=(10,20,30,40)
# print(i)

#another form declaration of tuple
# i=10,20,30,40
# print(type(i))

#changing elements in tuple method
# i=(10,20,30,40)
# t=list(i)
# t.append(50)
# t.append(60)
# t[2]=20
# print(t)
# k=tuple(i)
# print(k)
# print(k)


#functions of  tuple

#len()
# my_tuple=(10,20,30,40,)
# print(len(my_tuple))



#count()
# my_tuple=(10,20,30,40,40,30,20)
# print(my_tuple.count(40))


#sorted()
# my_tuple=(20,50,40,10,80)
# print(sorted(my_tuple))


#max() & min()

# my_tuple1=("abhi","venkatram","bhargav","sairam",)
# print(min(my_tuple1))
# print(max(my_tuple1))



#unpacking and packing
# colors=("blue","green","red")
# (cloud,grapes,apple)=colors
# print(cloud)
# print(grapes)
# print(apple)



# l=[i for i in range(0,10 )]
# print(l)


t=(i for i in range(0,10 ))
print(t)
