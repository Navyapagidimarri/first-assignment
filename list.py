l=[]
print(type(l))
#here we can define a list in square brackets only 

l=[1,"navya",15.45,1+3j,True,False,]
print(l)
#we can create a list whch we can collect diff types of elements like string,float,integer,boolean

l=[1,"navya","navya",1,15.67]
print(l)
#we can create a list with duplicate values also.it allows duuplicates

#Access the list with index method
 #    0        1       2        3         4
l=["apple","banana","mango","grapes","watermelon"]
print(l[2])
print(l[4])


#Access the list with slicing methd
l=["apple","banana","mango","grapes","watermelon"]
print(l[0:3])

#we can add elements with append method  ---append is the method to add the elementsat end
l=["apple","banana","mango","grapes","watermelon"]
l.append("pomogranate")
print(l)

#we can delet any tem from list with remove methoddelete method with slicing
l=["apple","banana","mango","grapes","watermelon"]
l.remove("apple")
del(l[2])
print(l)

#we can insert any item in specified index with insert method
l=["apple","cat","dog","elephant"]
l.insert(1,"ball")
print(l)

#we can extend the list with tuple fun also
l=["apple","ball","cat","dog","elephant"]
s=("fish","gun","hen")
l.extend(s)
print(l)

