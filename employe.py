def add_employee_details():
 d={}
 data=0
 entry_id=int(input("enter number of enteries"))
 for i in range(0,entry_id):
  emp_id=input("enter employee id:")
  if emp_id in d.keys():
    print("employee already registerd ,please enter valid employee_id:")
    emp_id=input("enter employee id:")
  emp_name=input("enter employee name:")
  emp_domain=input("enter eomployee  domain:")
  emp_email=input("enter email id:")
  d[emp_id]=emp_name,emp_email,emp_domain
  print("employee details added successfully")
  print(d)
  data=data+1
add_employee_details()
