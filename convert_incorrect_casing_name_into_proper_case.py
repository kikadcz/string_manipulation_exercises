#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

name = input("What's your full name? (Write in incorrect casing) :")

proper_case = (name.strip().title())

print(proper_case)