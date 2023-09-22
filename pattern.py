#90 degrees Traingle in reverse way
# for i in range(6,0,-1):
#     print("*"*i)


#90 degrees traingle in correct way
# for i in range(1,6):
#     print("*"*i)


n=int(input("enter number of rows"))
for i in range(n):
    for j in range(i):
        print("*",end =" ")
    print()