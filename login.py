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
#signup code
    for j in range(0,2):
        new_input_user=input("enter new username")
        if new_input_user==input_user:
            print("please enter new user")
            new_input_user1=input("enter new username")
        new_input_password=input("enter new password")
        new_input_confirm_password=input("enter password again")
        if new_input_password!=new_input_confirm_password:
            print("please enter again")
        else:
            d.update({new_input_user:new_input_confirm_password})
        d[new_input_user]=new_input_confirm_password
        print(d)
        print("all data registerrd successfully")
register()
def login():
    #with previous data alreday stored so we have do login with the same user only
    d = {'navya': '123456', 
         'kavitha': '234567',
          'anusha': '123456', 
          'mamatha': '1111'}
    for key,value in d.items():
      login_name=input("enter user login name")
      login_passwod=input("enter login password")
      if login_name in d.keys():
          print("login successfully")
      else:
          print( "please sign up for new login")
login()