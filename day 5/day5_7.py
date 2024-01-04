#password generator
import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']



symbols_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']


character = int(input("enter the lenght of password\n"))
number = int(input("enter the number you want\n"))
symbols = int(input("enter the symbol you want\n"))
password = ""

for _ in range(character):
    password += random.choice(alphabet_list)

for _ in range(number):
    password += random.choice(numbers_list)

for _ in range(symbols):
    password += random.choice(symbols_list)

# Shuffle the password to make the order random
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)
print("Generated Password:", password)