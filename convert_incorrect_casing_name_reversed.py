#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

name = input("What's your full name? (Write in incorrect casing) :")

reversed_case = name.swapcase()

print(reversed_case)