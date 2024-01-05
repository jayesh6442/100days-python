def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Encrypt only alphabetical characters
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Example usage:
message = input("enter the message")
shift_amount = int(input("enter the key"))

# Encryption
encrypted_message = encrypt(message, shift_amount)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, shift_amount)
print("Decrypted message:", decrypted_message)
