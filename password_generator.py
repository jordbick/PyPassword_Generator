import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_choice = int(input("How many letters would you like in your password? \n"))
numbers_choice = int(input("How many numbers would you like? \n"))
symbols_choice = int(input("How many symbols would you like? \n"))


password = ""

len(letters)

# continue loop to choose the correct number of letters for letter_choice
for choice in range(1, letters_choice+1):
    # generate a random number between 0 and length of list. Use this number as index for list to generate a random letter. Then add it to password
    letter = letters[random.randint(0, len(letters)-1)]
    password += letter

for choice in range(1, numbers_choice+1):
    number = numbers[random.randint(0, len(numbers)-1)]
    password += number

for choice in range(1, symbols_choice+1):
    symbol = symbols[random.randint(0, len(symbols)-1)]
    password += symbol


password = ''.join(random.sample(password, len(password)))

print(f"Here is your new password {password}")