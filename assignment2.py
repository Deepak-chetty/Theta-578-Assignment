import pandas as pd
screen_time = [2, 4, 6, 7, 8]
sleep_hours = [3, 7, 8, 2, 10]
stu_name = ["Deepak", "Nagesh", "SaiCharan", "Tanush", "Student"]

dict1 = {
    "screen_time" : screen_time,
    "sleep_hours" : sleep_hours,
    "stu_name" : stu_name
}

df = pd.DataFrame(dict1)
print(df)


dict1 = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

result = {key: value for key, value in dict1.items()}
print(result)

# 1. Even numbers using list comprehension
list = [1, 2, 3, 4, 5, 6, 7, 8]
res = [i for i in list if i % 2 == 0]
print("Even Numbers: ",res)

# 2. Check for palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Creating a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Deepak', 19, 'Hyderabad']
dictionary = dict(zip(keys, values))

# 4. Finding common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]

# 5. Finding list of squares
squares = [x**2 for x in range(1, 11)]

# 6. Finding even numbers from a list
numbers = [12, 7, 9, 20, 15, 30]
even_list = [x for x in numbers if x % 2 == 0]

# 7. Squares of a number using dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 11)}

# 8. Square roots of a number using tuple comprehension
import math
square_roots = tuple(math.sqrt(x) for x in range(1, 11))

# 9. Even numbers with list comprehension (repeated for emphasis)
even_list_comprehension = [x for x in range(1, 51) if x % 2 == 0]

# 10. Transform the string into uppercase
string = "hello world"
uppercase_string = string.upper()
