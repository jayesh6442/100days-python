alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


massage = input("enter the massge ")
shift = int(input("enter the shift amount "))

def encrption(plain_text,key):
        encrypted_text = ''
        for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + key
                new_letter = alphabet[new_position]
                encrypted_text += new_letter
        print(encrypted_text)
encrption(plain_text=massage,key=shift)


def decode(encrypted_text,key):
        plain = ''
        for letter in encrypted_text:
                position = alphabet.index(letter)
                actual_positin = position -  key
                plain += alphabet[actual_positin]
        print(plain)    
        
print=(decode(encrypted_text=massage,key=shift))


