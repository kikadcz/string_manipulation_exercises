#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

words = input("Input a complete statement : ")

words_count = len(words.split())

print("Number of words :", words_count)