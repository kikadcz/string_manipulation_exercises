#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

name = input("What's your name? (Include several space character before typing your name)")

name = name.strip()

print(f"Name:", name)

