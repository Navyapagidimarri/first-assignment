# class properties:
#     def m1(self):
#         self.name="pagidimarri"
        
# class phone(properties):
#       def m2(self):
#         self.myname="navya"
#         print(self.name+self.myname)
# c=phone()
# c.m1()
# c.m2()

class Samsung:
    brand = "Samsung"
    print("we love sumsung brand ,we hsve so many sumsung items with us.let's see my collection")
    def __init__(self, battery, price):
        self.price = "58000"
        self.battery = "100mh"

class FlipPhone(Samsung):
    def flip(self):
        self.model = "Galaxy S23"
        print("Flip phone features are", "price " ,self.price ,"battery" ,self.battery , "brand name", self.brand ,self.model)

class smartTv(Samsung):
    def Tv(self):
        self.model="2023"
        print("smart tv features are", "price " ,self.price ,"battery" ,self.battery , "brand name", self.brand ,self.model)
c = FlipPhone()
c.flip()
c1=smartTv()
c1.Tv()



