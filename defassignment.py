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





#3.write a python function to check string is panagram or not
# def pangram(string):
#     string = string.lower()
#     new_set = set()
#     for char in string:
#         if char.isalpha():
#             new_set.add(char)
#     return len(new_set) == 26
# input_str = "The quick brown fox jumps over the lazy dog"
# result = pangram(input_str)
# if result:
#     print("The input string is a pangram.")
# else:
#     print("The input string is not a pangram.")



#write a python code to sum all the elements
# def sum_function():
#     l=[8,2,3,0,7]
#     sum(l)
#     result=sum(l)
#     print(result)
# sum_function()



#write a function to define sum of arguments ,pass the values to the aruguments
# def sum_values(*args):
#     total = sum(args)
#     return total
# result = sum_values(1,3,4,5,6)
# print(result) 





#4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
# def print_squares():
#  squares_list = []
#  for number in range(1, 11):
#         square = number ** 2
#         squares_list.append(square)
#         print(squares_list)
# print_squares()

    
