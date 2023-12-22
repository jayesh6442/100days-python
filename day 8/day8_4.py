#ciper text generator


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode = input("enter encode or decode ")
massage= input("enter the massage")
shift=int(input("enter the shift"))


def encrypt(plain_text,shift_amount):
    cifer_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        new_letter = alphabet[new_position]
        cifer_text+=new_letter
    print(cifer_text)

encode(massage, encode)

#revisit the day 8 for me please 
 