input1=eval(input("enter elements"))
print("first entered list ",input1)
if len(input1)>=2:
     input1[0] , input1[-1]=input1[-1],input1[0]
print("second entered list ",input1)   