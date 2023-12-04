class atm():
    def __init__(self):
        self.balance = 1000
        self.pin = None
    def process(self):
        while True:
         print("welcome to the bank ")
         self.select_operation =input("Enter Operations 1/2/3/4/5")
         if self.select_operation in ["1","2","3","4","5"]:
            if self.select_operation =="1":
                object.pingenerate()
            if self.select_operation =="2":
                object.balancenquiry()
            if self.select_operation =="3":
                object.deposit()
            if self.select_operation=="4":
                object.withdraw()
            if self.select_operation=="5":
             break
    def pingenerate(self):
        while True:
         self.pin=(input("enter input number :"))
         self.enter_second_time=(input("enter input number :"))

         if self.pin!=self.enter_second_time:
           print("enter valid  pin ")
         else:
           print("pin generated successfully ")
           break
    def balancenquiry(self):
        print(self.balance)
        object.process()
    def deposit(self):
        self.deposit=int(input("Enter Amount to Deposit"))
        self.balance+=self.deposit
        print(self.balance)
        object.process()
    def withdraw(self):
        self.pin1=input("enter 4 digit pin")
        if self.pin1!=self.pin:
            print("enter proper pin")
        else:
            print("welcome ")     
        if True:
         self.withdraw=int(input("enter withdraw amount"))
         if self.balance>=self.withdraw:
            self.balance -= self.withdraw
            print("withdraw successsfully")
         else:
            print("amount not available in your account :")
            self.balance =self.balance-self.withdraw
            object.process()
    
object=atm()
object.process()


