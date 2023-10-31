class DairyFarm:
    buffalo = "Total 10 buffaloes"

    def __init__(self, brand):
        self.__brand = brand

    def single_customer(self):
        self._single = 70
        print("For those who buy in small quantities - price details are 70/liter")

    def bulk_customer(self):
        self._bulk = 60
        print("For those who purchase more than 20 liters per day, cost of milk is 60/liter")

class Income(DairyFarm):
    def count_income(self):
        self.daily_sale = int(input("How many liters did you deliver to your customers: "))
        self.delivery_count = self.daily_sale * self._single
        return self.delivery_count

    def count_bulk_income(self):
        self.bulk_sale = int(input("How many liters will you sell today at the center: "))
        self.centre_sale = self._bulk * self.bulk_sale
        return self.centre_sale

    def total_income(self):
        self._delivery_count = self.count_income()
        self._centre_sale = self.count_bulk_income()
        self.total = self._delivery_count + self._centre_sale
        self.monthly_income = self.total * 30
        print("Monthly income:", self.monthly_income)

class Expenditure(Income):
    def exp(self):
        self._dhana = 50000
        self._salaries = 40000
        expenditure = self._dhana + self._salaries
        final_amount = self.monthly_income - expenditure
        print("Final amount:", final_amount)

farm = Expenditure("Shanmukh DairyFarm")
print("Welcome to the dairy farm", farm._DairyFarm__brand)
farm.single_customer()
farm.bulk_customer()
farm.total_income()
farm.exp()
