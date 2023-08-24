#dict methods
#length()
# d={1:"white",2:"black",3:"blue"}
# print(len(d))



# d={1:"white",2:"black",3:"blue"}
# print(d.get(4))#it will show none
# print(d[4])#it will get key error



#dict respresesntation in key:value
# d={
# "nursery":"g.Bhargav ram",
# "4thclass":"abhiram"
# }
# d["5thclass"]="navya"#adding elements
# print(d)




# d={1:"white",2:"black",3:"blue"}#items() for using 
# for key,value in d.items():
#    print(key,value)



# d={1:"white",2:"black",3:"blue"}#items() for using 
# for y in d.values():
#     print(y)


# d={"boys":{"abhiram":"4thclass",
#                "bhargavram":"nursery"},
#    "girls":{"navya":"inter","smitha":"degree"}
# }
# print(d["girls"]["smitha"])


d={"boys":{"abhiram":"4thclass",
               "bhargavram":"nursery"},
   "girls":{"navya":"inter","smitha":"degree"}
   }
print(d.pop(0))
print(d)
#print(d.popitem())#it returns lat inserted index
#print(d)


