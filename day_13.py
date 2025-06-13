
#3

items = input("Enter comma-separated words: ")
words = items.split(',')             # Step 1: split by comma
words.sort()                         # Step 2: sort alphabetically
print(",".join(words))               # Step 3: join with comma and print

#4

text = input("Enter space-separated words: ")
words = text.split()                 # Step 1: split by space
unique_words = sorted(set(words))   # Step 2: remove duplicates and sort
print(" ".join(unique_words))       # Step 3: join with space and print


#5
text = input("Enter a sentence: ")

letters = 0
digits = 0

for char in text:
    if char.isalpha():      # checks if character is a letter (a-z or A-Z)
        letters += 1
    elif char.isdigit():    # checks if character is a digit (0-9)
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)


#6

import re

input_passwords = input("Enter comma-separated passwords: ").split(',')
valid_passwords = []

for password in input_passwords:
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        valid_passwords.append(password)

print(",".join(valid_passwords))



