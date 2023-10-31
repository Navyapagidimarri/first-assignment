class dairyfarm:
    buffelow="toral 10 buffelows "
    def __init__(self,brand):
        self.brand="shanmukh dairyfarm"
    def singlecustomer(self):
        self.single=70
        print("for hose supply- price deatils are 70/letre")
    def bulkcutomer(self):
        self.bulk=60
        print("who are purchase morethan 20 letres per day cost of milk is 60/letre")
class income(dairyfarm):
    def countincome(self):
        self.daily_sale=int(input("how many leters you delivered to out customer : "))
        self.delivery_count=self.daily_sale * self.single
        return self.delivery_count
    def countbulkincome(self):
        self.bulk_sale=int(input("how many leters you will sale today in centre :"))
        self.centre_sale=(self.bulk*self.bulk_sale)
        return self.centre_sale
    def totalincome(self):
        self.total=int(self.delivery_count + self.centre_sale )
        self.monthlyincome=self.total*30
        print(self.monthlyincome)
class expenditure(income):
    def exp(self):
        self.dhana=50000
        self.salaries=40000
        expenditure=self.dhana + self.salaries
        final_amount=self.monthlyincome - expenditure
        print(final_amount)
c=expenditure("shanmukh dairy farm")
c.singlecustomer()
c.bulkcutomer()
c.countincome()
c.countbulkincome()
c.totalincome()
c.exp()

