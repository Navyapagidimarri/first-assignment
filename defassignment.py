#1.Write a Pythonfunction that accepts a string and counts the number of upper and lower case letters.
# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     print("Uppercase count:", upper_count)
#     print("Lowercase count:", lower_count)
# count_upper_lower("Am Working In MArolix")




#2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def distinct_elements(input_list):
#     new_set = set()
#     for item in input_list:
#         new_set.add(item)
#     distinct_list = list(new_set)
#     return distinct_list
# input_list = [1, 2, 2, 3, 4, 4, 5]
# distinct_elements = distinct_elements(input_list)
# print(distinct_elements)



#3.write a function to find sum of given values, pass values has variable number of arguments to function.
# def calculate_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# result = calculate_sum(1, 2, 3, 4, 5)
# print(result) 



#4.Write a Python function to sum all the numbers in a list.
# def sum_numbers(n):
#     total_sum = sum(n)
#     return total_sum
# numbers = [1, 2, 3, 4, 5]
# total = sum_numbers(numbers)
# print("Sum of numbers:", total)

#write a python function to check string is panagram or not
def pangram(string):
    string = string.lower()
    new_set = set()
    for char in string:
        if char.isalpha():
            new_set.add(char)
    return len(new_set) == 26
input_str = "The quick brown fox jumps over the lazy dog"
result = pangram(input_str)
if result:
    print("The input string is a pangram.")
else:
    print("The input string is not a pangram.")


#5.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
# def print_squares():
#  squares_list = []
#  for number in range(1, 11):
#         square = number ** 2
#         squares_list.append(square)
#         print(squares_list)
# print_squares()


