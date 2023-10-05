def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choose_operation = input("Enter choice (1/2/3/4): ")

        if choose_operation in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choose_operation == '1':
                print("Result:", add(num1, num2))
            elif choose_operation == '2':
                print("Result:", subtract(num1, num2))
            elif choose_operation== '3':
                print("Result:", multiply(num1, num2))
            elif choose_operation == '4':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid input. Please try again.")
            break

       
calculator()