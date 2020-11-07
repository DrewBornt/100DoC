import random

# Overly complex passwords without use of an encrypted password manager is actually counterintuitive
# But this is just an exercise

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
 
letterNum = int(input("How many letters would you like in your password?\n"))

symbolNum = int(input("How many symbols would you like in your password?\n"))

numberNum = int(input("How many numbers would you like in your password?\n"))

password_characters = []

for letter in range(letterNum):
    password_characters.append(random.choice(letters))
for symbol in range(symbolNum):
    password_characters.append(random.choice(symbols))
for number in range(numberNum):
    password_characters.append(random.choice(numbers))

random.shuffle(password_characters)

password = ""

for character in password_characters:
   password += character

print(f"Your password is {password}")