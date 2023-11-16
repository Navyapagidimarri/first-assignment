class career:
    def __init__(self):
        self.list={}
        self.applications={}
class admin(career):
    def create(self):
        self.post=input("enter POst details : ")
        self.qualification=input("enter qulaification  details : ")
        self.numberofjobs=input("enter number of jobs : ")
        self.place=input("enter working place : ")
        self.salary=input("enter package details :")
        self.workinghours=input("enter timings work ")
        self.list[self.post]={"qulification:" :self.qualification,
                                 "number of jobs" :self.numberofjobs,
                                 "place":self.place,
                                 "salary":self.salary,
                                 "workinghours":self.workinghours}
        print(self.list)
    def display(self):
        print("Available job Posts are :",self.list)
    def update_job(self):
        updated_post=input("enter POst name : ")
        if updated_post in self.list.keys():
            self.qualification = input("Enter new qualification details: ")
            self.number_of_jobs = input("Enter new number of jobs: ")
            self.place = input("Enter new working place: ")
            self.salary = input("Enter new package details: ")
            self.workinghours = input("Enter new working hours: ")
            self.list[updated_post] = {
                "qualification": self.qualification,
                "number of jobs": self.number_of_jobs,
                "place": self.place,
                "salary": self.salary,
                "working hours": self.workinghours
            }
            print("Details updated successfully.")
            print(self.list)
        else:
            print("Job not found.")
    def delete(self):
            enter_post=input("enter post details")
            if enter_post in self.list:
                del self.list[self.post]
                print(f"deleted {self.post}sucessfully")
            else:
                print("post not found !")
    def apply(self):
        self.job_post_apply=input("enter job post :")
        self.name=input("enter name:")
        self.qualification=input("enter qulaification details of employee :")
        while True:
            self.mobilenumber=input("enter mobile number")
            if self.mobilenumber.isdigit():
              if len(self.mobilenumber)!=10:
                print("enter 10 digit mobile number :")
              else:
                break
            else:
                print("enter numrical numbers only")
        self.email_id=input("enter your gamil id :")
        if self.email_id.endswith(".com"):
              print("Thank you for your responce :")
        else:
            print("Invalid mail id")
        if True:
            print("congratulation you will get call from company")
            self.applications[self.job_post_apply]={
                                    "name":self.name,
                                    "qualification ":self.qualification,
                                    "mobilenumber":self.mobilenumber,
                                    
                                    "email_id":self.email_id

        }
    def display_applications(self):
        print(self.applications)

class user(admin):
      def user_entry(self):
        job_list = super().display()
        print("Job Details:")
        for job, details in job_list.items():
            print(f"Post: {job}")
            for key, value in details.items():
                print(f"{key}: {value}")
      def user_wantto_apply(self):
         super().apply()
us=user()
while True:
      print("\nMenu:")
      print("1. create a post  :")
      print("2. update a post :")
      print("3. delete post : ")
      print("4. view job posts : ")
      print("5.view applications for the job -checking by admin")
      print("1. Apply for the job -user : ")
      choose_option=int(input("enter option 1/2/3/4/5/6/7 : "))

      if choose_option==1:
        us.create()
      elif choose_option==2:
        us.update_job()
      elif choose_option==3:
        us.delete()
      elif choose_option==4:
        us.display()
      elif choose_option==5:
        us.apply()
      elif choose_option==6:
        us.display_applications()
      elif choose_option==7:
        break
