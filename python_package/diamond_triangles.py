# def my_function2():
#     for i in range(1, 21, 2):
#         asterik = "*" * i
#         print(f"{asterik:<2}")
#
#
# print(my_function2())
# print()


def my_function(number: int):
    for i in range(1, number + 1):
        asterik = " *" * i
        print(asterik, end="\n")


print(my_function(10))


def my_square(number: int):
    for count in range(1, number + 1):
        if count == 1 or count == number:
            print("* " * number)
        else:
            in_between = " " * ((number * 2) - 3)
            print("*{a}*".format(a=in_between))


print(my_square(20))
# for i in range(1, 21, 2):
#     asterik = "*" * i
#     print(f"{asterik:<2}")
# print()
#
# for i in range(1, 21, 2):
#     asterik = "*" * i
#     print(f"{asterik:>21}")
# print()
# for i in range(21, 0, -2):
#     asterik = "*" * i
#     print(f"{asterik:<2}")
# print()
# for i in range(21, 0, -2):
#     asterik = "*" * i
#     print(f"{asterik:>21}")
