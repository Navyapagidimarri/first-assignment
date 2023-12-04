class school:
 def enter(self):
  school=eval(input("enter"))
  data={}
  for i in range(school):
    name=input("enter name :")
    fathername=input("enter father name :")
    mothername=input("enter mother name :")
    age=int(input("enter age"))
    admission=input("class admission")
    data[name]=fathername,mothername,age,admission
    print("details enteed successfully ")
  def display(self):
    print(f"Student name:{name},fathernameis:{fathername},mothername is:{mothername},age is: {age},admission is,{admission}")

obj=school()
obj.enter()
obj.display()

