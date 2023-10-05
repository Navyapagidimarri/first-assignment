from user_package.register_1.register import*
entry=int(input("enter number of customers"))
for i in range(1,entry+1):
 input_name=input("enter name")
 input_password=input("enter password")
 while True:
    input_confirm_password=input("enter input password")
    if input_password!=input_confirm_password:
       print("enter same password as before ")
       break
 obj = Register(name=input_name, password=input_password, confirm_password=input_confirm_password)
 obj.display()
 print("successfully registered ",i,"customers")
