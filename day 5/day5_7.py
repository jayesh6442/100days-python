#password generator
import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']



symbols_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

password= []

ch = int(input("enter the number of char: \n"))
number = int(input("enter the number of number: \n"))
symbol = int(input("enter the number of symbol: \n"))

for char in range (1,ch+1):
    password+= random.choice(alphabet_list)
for char in range (1,number+1):
    password += random.choice(numbers_list)
for char in range (1,symbol+1):
    password += random.choice(symbols_list)
#easy lavel
print(password)

#hard level

random.shuffle(password)
print(password)

strinpassword = ''

for i in password:
    strinpassword +=i

print(strinpassword)