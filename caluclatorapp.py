class caluclator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
         print(self.num1 + self.num2)

    def subtract(self):
         print(self.num1 - self.num2)

    def multiply(self):
         print( self.num1 * self.num2 )

    def divide(self):
         if self.num2 != 0:
          print(self.num1 / self.num2)
         else:
          return "Cannot divide by zero"

    def m1(self):
        while True:
           print("Select operation:")
           print("1. Addition")
           print("2. Subtraction")
           print("3. Multiplication")
           print("4. Division")
           choose_operation = input("Enter choice (1/2/3/4): ")
           if choose_operation in ['1', '2', '3', '4']:
                if choose_operation == '1':
                    result = self.add()
                elif choose_operation == '2':
                    result = self.subtract()
                elif choose_operation == '3':
                    result = self.multiply()
                elif choose_operation == '4':
                    result = self.divide()

                break
           else:
                print("Invalid input. Please try again.")
e1=caluclator()
e1.m1()