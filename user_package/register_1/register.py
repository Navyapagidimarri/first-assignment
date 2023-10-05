class Register:
    def __init__(self,name,password,confirm_password):
        self.name=name
        self.password=password
        self.confirm_password=confirm_password
    def display(self):
        print("login:",self.name)
        print("password",self.password)
        print("confirm password",self.confirm_password)
        print("-----------------")



 