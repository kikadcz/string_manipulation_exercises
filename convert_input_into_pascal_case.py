#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

name = input("What's your full name? : ")

pascal_name = "".join(name.title().split())

print(pascal_name)

