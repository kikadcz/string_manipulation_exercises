#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

name = input("What's your full name? (Use incorrect casing): ")

snake_case = "_".join(name.lower().split())

print(snake_case)