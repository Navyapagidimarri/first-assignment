class hospital:
    def __init__(self):
        self.d={}
    def entry(self):
        self.Enter_name=input("enter name of the patient")
        self.Enter_problem=input("Enter issue of the patient")
        self.Enter_joining_date=input("Enter joining date (dd -mm-yyyy)")
        self.d[self.Enter_name]=self.Enter_problem,self.Enter_joining_date
        print(self.d)
    def display(self):
        for  i,j in self.d.items():
         print("patient name is",i)
         print("patient problem is ",j[0])
         print("patient joining date",j[1])
         print(self.d)
    def delete(self):
        self.enter_key_to_delete=input("enter name to delete")
        if self.enter_key_to_delete in self.d:
            del self.d[self.enter_key_to_delete]
            print("removed successfully ")
    def process(self):
        while True:
            print("for enter patient deatils press 1")
            print("for display patient name press 2")
            enter_key=int(input("enter key to press 1/2/3"))
            if enter_key==1:
                self.entry()
            elif enter_key==2:
                self.display()
            elif enter_key==3:
                self.delete()
            else:
                print("thanks for visiting")
                break
hos=hospital()
hos.process()


