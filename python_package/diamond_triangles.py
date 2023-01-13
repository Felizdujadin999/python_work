def my_function2():
    for i in range(1, 21, 2):
        asterik = "*" * i
        print(f"{asterik:<2}")
    for i in range(21, 0, -2):
        asterik = "*" * i
        print(f"{asterik:2}")


print(my_function2())
print()

asteriks = int(input("Enter number of asteriks: "))


def my_function(input_):
    for i in range(1, input_ + 1):
        asterik = " *" * i
        print(asterik, end="\n")


my_function(asteriks)

square = int(input("Enter number of asteriks:"))


def my_square(input):
    for count in range(1, input + 1):
        if count == 1 or count == input:
            print("* " * input)
        else:
            in_between = " " * ((input * 2) - 3)
            print("*{b}*".format(b=in_between))


my_square(square)
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
