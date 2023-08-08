#l=[]
#print(type(l))
#here we can define a list in square brackets only 


#l=[1,"navya",15.45,1+3j,True,False,]
#print(l)
#we can create a list whch we can collect diff types of elements like string,float,integer,boolean





#l=[1,"navya","navya",1,15.67]
#print(l)
#we can create a list with duplicate values also.it allows duuplicates






#Access the list with index method
 #    0        1       2        3         4
#l=["apple","banana","mango","grapes","watermelon"]
#print(l[2])
#print(l[4])




#Access the list with slicing methd
#l=["apple","banana","mango","grapes","watermelon"]
#print(l[0:3])



#we can add elements with append method  ---append is the method to add the elementsat end
#l=["apple","banana","mango","grapes","watermelon"]
#l.append("pomogranate")
#print(l)



#we can delet any tem from list with remove methoddelete method with slicing
#l=["apple","banana","mango","grapes","watermelon"]
#l.remove("apple")
#del(l[2])
#print(l)



# pop method to remove item with index 
#l=["apple","banana","mango","grapes","watermelon"]
#l.pop(1)
#print(l)




#pop method we dont declare any index automativcally last element will remove
#l=["apple","banana","mango","grapes","watermelon"]
#l.pop()
#print(l)



#clear()  will give empty list
#l=["apple","banana","mango","grapes","watermelon"]
#l.clear()
#print(l)


#append()we can add items to empty list by perfect order list always follow insertion order
#l=[]
#l.append("red")
#l.append("blue")
#l.append("yellow")
#l.append("black")
#l.append("green")
#l.append("white")
#l.append("grey")
#print(l)




#loops in for loop will pfrint items in colomun 
#l=['red', 'blue', 'yellow', 'black', 'green', 'white', 'grey']
#for x in l:
#   print(x)



#range in for loop here we can access index number in line
#l=['red', 'blue', 'yellow', 'black', 'green', 'white', 'grey']
#for x in range(len(l)):
#    print(x)


#l=['red', 'blue', 'yellow', 'black', 'green', 'white', 'grey']
#i=0
#while i<len(l):
#   print(i)
#    i=i+1



#we can insert any item in specified index with insert method
#l=["apple","cat","dog","elephant"]
#l.insert(1,"ball")
#print(l)








#we can extend the list with tuple fun also
#l=["apple","ball","cat","dog","elephant"]
#s=("fish","gun","hen")
#l.extend(s)
#print(l)


#sort() method used to annage words alpahbetical order
#l=['red', 'blue', 'yellow', 'black', 'green', 'white', 'grey']
#l.sort()
#print(l)