
# l=(1,2,3,4,5,6)
# result=tuple(map(lambda n:n*2,l))#map(function,sequance)result=list(map(multiply,l))#
# print(result)#here we can get location of functin


# s="am working in marolix"
# result=tuple(map(lambda s:list(s),s))
# print(result)




#calculate Length of Strings in a List:
# def length(string):
#    return len(string)
# l=["blue","white","black"]
# output=list(map(length,l))
# print(output)



#converting words to upper
# check_1=["navya","anusha","rushitha","gayathri"]
# def convert_upper(x):
#    return x.upper()
# result=list(map(convert_upper,check_1))
# print(result)



l=["1","2","3","4"]
result=list(map(lambda s: int(s),l))
print(result)
