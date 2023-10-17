class SamsungCart:
    def __init__(self):
        self.items = {"tv": 50000, "mobile": 10000, "refrigerator": 25000}
        self.added_items = {}

    def add_item(self, item, quantity):
        item = item.lower()
        if item in self.items:
            if item in self.added_items:
                self.added_items[item] += quantity
            else:
                self.added_items[item] = quantity
            print(f"{quantity} {item} added to the cart.")
        else:
            print("Invalid item. Please select a valid item.")

    def remove_item(self):
        select_item = input("Enter item from added list (tv, mobile, refrigerator): ").lower()
        if select_item in self.added_items:
            quantity = int(input("Enter the quantity to remove: "))
            if quantity >= self.added_items[select_item]:
                del self.added_items[select_item]
                print(f"All {select_item}s removed from the cart.")
            else:
                self.added_items[select_item] -= quantity
                print(f"{quantity} {select_item} removed from the cart.")
            print("Updated cart:", self.added_items)
        else:
            print("Item not found in the cart.")

    def update_item_quantity(self):
        select_item = input("Enter the item you want to update (tv, mobile, refrigerator): ").lower()
        if select_item in self.items:
            additional_quantity = int(input("Enter the additional quantity: "))
            self.added_items[select_item] += additional_quantity
            print(f"Quantity of {select_item} updated to {self.added_items[select_item]}.")
        else:
            print("Item not found in the cart.")

    def calculate_total_bill(self):
        total_bill = 0
        for item, quantity in self.added_items.items():
            total_bill += self.items.get(item, 0) * quantity
        return total_bill


cart = SamsungCart()
while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Update item quantity")
    print("4. Calculate total bill")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item name (tv, mobile, refrigerator): ")
        quantity = int(input("Enter quantity: "))
        cart.add_item(item, quantity)
    elif choice == 2:
        cart.remove_item()
    elif choice == 3:
        cart.update_item_quantity()
    elif choice == 4:
        total_bill = cart.calculate_total_bill()
        print("Total bill to pay:", total_bill)
    elif choice == 5:
        print("thanks for choosing us")
        break
    else:
        print("Invalid choice. Please try again.")
