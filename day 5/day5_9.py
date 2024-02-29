import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
password= []


char = int(input("enter the char: "))
numb = int(input("enter the numbs: "))
sy = int(input("enter the symbols: "))


for i in range(1,char+1):
    password += random.choice(alphabet_list)

for i in range(1,numb+1):
    password += random.choice(numbers_list)

for i in range(1,sy+1):
    password += random.choice(symbols_list)


random.shuffle(password)

passas_string  = ''

for i in password:
    passas_string +=i
print(passas_string)