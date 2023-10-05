#Adding all employee details to the dictinary 
#def add_employee_details():
#  d={}
#  employ_entry=int(input("enter keys:"))
#  for i in range(employ_entry):
#   emp_id=input("enter employee id:")
#   emp_name=input("enter employee name:")
#   emp_domain=input("enter domain domain:")
#   emp_email=input("enter email id:")
#   d[emp_domain]=emp_name,emp_email,emp_id
#   print(emp_domain,":",emp_name)
# add_employee_details()


# def employee_details():
#     d = {}
#     employ_entry = int(input("Enter the number of employes: "))
#     for i in range(employ_entry):
#         emp_name = input("Enter employee name: ")
#         emp_domain = input("Enter domain: ")
#         emp_id=input("enter employee id:")
#         emp_email=input("enter email id:")
#         d[emp_name]=emp_id,emp_email,emp_domain,emp_name
#         print(d)
#     print("Employee details:")
#     print("*****************")
#     for domain, name in d.items():
#      if emp_domain in d:
#         d[emp_domain].append(emp_name)
#         print("Domain:", domain)
#         print("Employee Names:", name)
# employee_details()



# def employee_details():
#     d = {}  # Dictionary to store employee details by domain
#     employ_entry = int(input("Enter the number of employees: "))
#     for i in range(employ_entry):
#         emp_name = input("Enter employee name: ")
#         emp_domain = input("Enter domain: ")
#         emp_id = input("Enter employee id: ")
#         emp_email = input("Enter email id: ")
#         if emp_domain in d:
#             d[emp_domain].append((emp_name, emp_id, emp_email))
#         else:
#             d[emp_domain] = [(emp_name, emp_id, emp_email)]
#         print(d)
#     print("Employee details:")
#     print("*****************")
#     for domain, employees in d.items():
#         print("Domain:", domain)
#         print("Employee Details:")
#         for emp in employees:
#             emp_name, emp_id, emp_email = emp
#             print("Employee Name:", emp_name)
#             print("Employee ID:", emp_id)
#             print("Employee Email:", emp_email)

# employee_details()

def employee_details():
    d = {}
    employ_entry = int(input("Enter the number of employees: "))
    for i in range(employ_entry):
        emp_name = input("Enter employee name: ")
        emp_domain = input("Enter domain: ")
        emp_id = input("Enter employee id: ")
        emp_email = input("Enter email id: ")
        d[emp_name] = [emp_name, emp_id, emp_email, emp_domain]
    return d

def filter_employees(d):
    print("Choose an option to filter:")
    print("1) Employee domain")
    print("2) Employee id")
    print("3) Employee email")
    print("4) Employee name")

    choose_option = int(input("Select an option (1/2/3/4): "))

    if choose_option == 1:
        particular_domain = input("Enter a particular domain: ")
        filtered_employees={}
        for key , value in d.items(): 
          if value[3] == particular_domain:
           filtered_employees[key]=value
        print(filtered_employees)

    elif choose_option == 2:
        particular_id = input("Enter employee ID: ")
        filtered_employees={}
        for key , value in d.items(): 
          if value[1] == particular_id:
           filtered_employees[key]=value
        print(filtered_employees)

    elif choose_option == 3:
        particular_email = input("Enter email: ")
        filtered_employees={}
        for key , value in d.items(): 
          if value[2] == particular_email:
           filtered_employees[key]=value
        print(filtered_employees)

    elif choose_option == 4:
        particular_name = input("Enter name: ")
        filtered_employees={}
        for key , value in d.items(): 
          if value[0] == particular_name:
           filtered_employees[key]=value
        print(filtered_employees)

    else:
        print("Invalid option. Please select a valid option (1/2/3/4).")

employee_data = employee_details()
filter_employees(employee_data)

    