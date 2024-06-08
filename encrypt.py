import random

class Code:
    def __init__(self):
        self.ascii_map = {i: chr(i) for i in range(128)}
    
    def Generatekey(self):
        keys = list(range(128))
        values = keys.copy()
        random.shuffle(values)
        encrypt_key = {keys[i]: values[i] for i in range(len(keys))}
        decrypt_key = {value: key for (key, value) in encrypt_key.items()}
        return encrypt_key, decrypt_key

    def encrypt(self, text, encryption):
        encoding = ''.join(chr(encryption[ord(char)]) if ord(char) in encryption else char for char in text)
        return encoding

    def decrypt(self, text, decryption):
        decoding = ''.join(chr(decryption[ord(char)]) if ord(char) in decryption else char for char in text)
        return decoding

# Generate keys for encryption and decryption
code_instance = Code()
keygen = code_instance.Generatekey()

# Encrypt a message
message = input("Enter Message You'd Like to encrypt: ")
encrypted_message = code_instance.encrypt(message, keygen[0])
print(f'Encrypted Message: {encrypted_message}')
print(f'Decryption Key: {keygen[1]}')  # Show the decryption key for reference

# Prompt user for the decryption key and the encrypted message to decrypt
decryption_key_input = input("Enter the decryption key (in the format '{k1: v1, k2: v2, ...}'): ")
encrypted_message_input = input("Enter the encrypted message: ")

# Convert the input decryption key from string to dictionary
decryption_key = eval(decryption_key_input)

# Decrypt the message
decrypted_message = code_instance.decrypt(encrypted_message_input, decryption_key)

print(f'Decrypted Message: {decrypted_message}')
