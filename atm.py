class Banking:
    def __init__(self, balance):
        self.pin = None
        self.balance = balance

    def functions(self):
        while True:
            print("\nOptions:")
            print("pin generation-1")
            print("deposit-2")
            print("withdraw-3")
            print("balance-enquiry")
            print("exit-0")
            user_choice = input("Enter your selected process: (1-4)")

            if user_choice == "1":
                self.pin_generate()
            elif user_choice == "2":
                self.deposit()
            elif user_choice == "3":
                self.withdraw_money()
            elif user_choice == "4":
                self.balance_enquiry()
            elif user_choice == "0":
                print("Thank you! Visit again.")
                return
            else:
                print("Invalid choice.try again later")

    def pin_generate(self):
        print("Generate a new pin ")
        while True:
            input_user_pin = input("Enter 4-digit pin: ")
            if len(input_user_pin) == 4 and input_user_pin.isdigit():
                self.pin = input_user_pin
                print("Successfully generated pin:", self.pin)
                break
            else:
                print("Invalid pin. Enter a 4-digit pin.")

    def balance_enquiry(self):
        print("Your account balance is:", self.balance)

    def deposit(self):
        deposit_amount = int(input("Enter the amount to deposit: "))
        self.balance += deposit_amount
        print("Deposit successful. Updated balance:", self.balance)

    def withdraw_money(self):
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print("Please collect the amount.")
        else:
            print("Insufficient funds")

bank = Banking(1000)
print("Welcome to Marolix Banking! Thanks for choosing us.")
bank.functions()
print("Updated account details:", bank.__dict__)