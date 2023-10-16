# class marolix_cart:
#        def add_product(self,item,price):
#           self.item=item
#           self.price=price
# ran=int(input("enter range of items"))
# shopping_cart={}
# for i in range(ran):
#   input_item=input("name of the item")
#   input_price=int(input("cost of that item"))
#   print(input_item ,":" ,input_price)
#   shopping_cart[input_item]=[input_price]
#   for item,price in shopping_cart.items():
#     print(shopping_cart)
# class buy(marolix_cart):
#     enter_wanted_product=input("enter wanted product")
#     total_cart=0
#     if enter_wanted_product in shopping_cart:
#         for i in shopping_cart.values:
#             total_cart=total_cart+i
#             print(total_cart)


class MarolixCart:
    def __init__(self):
        self.shopping_cart = {}

    def add_product(self, item, price):
        self.shopping_cart[item] = price

    def display_cart(self):
        print("Shopping Cart:")
        total_cost = 0
        for item, price in self.shopping_cart.items():
            print(f"{item} - Price: ${price}")
            total_cost += price

        print(f"Total Cost: ${total_cost}")


class Buy(MarolixCart):
    def calculate_total(self):
        total_cart = sum(self.shopping_cart.values())
        return total_cart


if __name__ == "__main__":
    ran = int(input("Enter range of items: "))
    shopping_cart = {}

    for i in range(ran):
        input_item = input("Name of the item: ")
        input_price = int(input("Cost of that item: "))
        print(input_item, ":", input_price)
        shopping_cart[input_item] = input_price

    cart = Buy()
    cart.shopping_cart = shopping_cart
    cart.display_cart()

    enter_wanted_product = input("Enter wanted product: ")
    if enter_wanted_product in shopping_cart:
        total_cart = cart.calculate_total()
        print("Total cost for", enter_wanted_product, "is: $", total_cart)
    else:
        print("Product not found in the shopping cart.")
