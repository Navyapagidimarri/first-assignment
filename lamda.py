# def lambda_function1(n):
#   return lambda a : a * n
# double_value = lambda_function1(2)
# print(double_value(10))



def even_lambda():
  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = (lambda x: x % 2 == 0, numbers)
print(even_numbers)