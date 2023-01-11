from array import *

#
# nums = array("i", [5, 3, 5, 6, 7])
# print(len(nums))

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 4, 5, 6, 8, 5, 6, 7, 8, 9, 10]
# numbers.append("Felix")
# numbers.insert(3, "Dujadin")
c_14 = numbers.copy()
count = c_14.count(6)
print(count)
# print(c_14)
# print(numbers)
# print(numbers[-4:-11:-2])
#
# sentence = "Felix is a backend engineer"
# print(sentence[9:5:-1])


set_value = {"precious", "Felix"}
user_input = list(input("Enter a list: "))
count = 0
for i in range(len(user_input)):
    if user_input[1] != set_value:
        set_value.add(user_input[1])
    else:
        count += 1
        print(user_input[1])
