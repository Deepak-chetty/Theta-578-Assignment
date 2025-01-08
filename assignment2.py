# import pandas as pd
# screen_time = [2, 4, 6, 7, 8]
# sleep_hours = [3, 7, 8, 2, 10]
# stu_name = ["Deepak", "Nagesh", "SaiCharan", "Tanush", "Student"]

# dict1 = {
#     "screen_time" : screen_time,
#     "sleep_hours" : sleep_hours,
#     "stu_name" : stu_name
# }

# df = pd.DataFrame(dict1)
# print(df)


# list = [1, 2, 3, 4, 5, 6, 7, 8]
# res = [i for i in list if i % 2 == 0]
# print("Even Numbers: ",res)


dict1 = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

result = {key: value for key, value in dict1.items()}
print(result)