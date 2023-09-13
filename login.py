#login_page---here am taking login and password

# d={
#        "navya":"123456",
#        "anusha":"234567",
#        "madhugayathri":"567890",
#        "rishika":"456789"

#       }
# for key,value in d.items():
#     if d[key]==value:
#         print("login successfully")
#     else:
#         print( "please sign up for new login")


#login - new login
# def login_page():
#     d={
#        "navya":"123456",
#        "anusha":"234567",
#        "madhugayathri":"567890",
#        "rishika":"456789"

#       }
#     for key,value in d.items():
#      key=input("enter a valid key:")
#      value=input("enter a valid value")
#     if d[key]==value:
#      print("correct")
#     else:
#      print("please try again")
#     for k in range(0,3):
#       key=input("enter new username:")
#       value=input("passwords:")
#       d[key]=value
#       print(d)
#     enter_key=input("enter a key")
#     enter_value=input("enter a value")
#     if enter_key in d.keys():
#      print("key already exists")
#     else:
#      d.update({enter_key:enter_value})
#     print(d)
# login_page()


#register
def register():
    d={}
    for i in range(0,2):
          input_user=input("username")
          input_password=input("password")
          d[input_user]=input_password
          print(d)
register()
