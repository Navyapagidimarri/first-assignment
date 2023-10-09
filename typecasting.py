#int 
# a=10
# b=type(a)
# print(b)


# a=12.15#double
# print(int(a))

# b=True
# print(int(b))


a=int(input("enter rows:"))
for i in range(a):
    for j in range(i):
        print( "*",end="" )
    print()