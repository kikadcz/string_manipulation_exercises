#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

number = int(input("Enter a number from 1-1000 :"))

padded_number ="{:0>6}".format(number)

print(padded_number)