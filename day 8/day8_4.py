alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("enter 'endcode'or 'decode ' operation: ")
massage= input("enter the message: ").lower()
shift = int(input("enter the shifit amount: "))
def encryption(plaintext,key):
        cipertext = ""
        for letter in plaintext:
                position = alphabet.index(letter)
                new_position = position+key
                new_letter = alphabet[new_position]
                cipertext+=new_letter
        print(cipertext)

def decryption(cipertext,key):
        plaintext = ""
        for letter in cipertext:
                position = alphabet.index(letter)
                new_position = position - key
                new_letter = alphabet[new_position]
                plaintext+=new_letter
        print(plaintext)
if direction == "endcode":
        encryption(massage,shift)
elif direction =="decode":
        decryption(massage,shift)
else:
        print("enter the valid input")