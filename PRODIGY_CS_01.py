#Encryption
def encrypt_text(plain_text, n):
    result = ""
    for ch in plain_text:
        if ch == " ":
            result += " "
        elif ch.isupper():
            result += chr((ord(ch) + n - 65) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) + n - 97) % 26 + 97)
        else:
            result += ch  
    return result

#Decryption
def decrypt_text(cipher_text, n):
    result = ""
    for ch in cipher_text:
        if ch == " ":
            result += " "
        elif ch.isupper():
            result += chr((ord(ch) - n - 65) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - n - 97) % 26 + 97)
        else:
            result += ch  
    return result


# Encryption
plain_text = input("Enter message to encrypt: ")
key = int(input("Enter the key to encrypt: "))
print("\n--- Encryption ---")
print("Plain Text    :", plain_text)
print("Shift Pattern :", key)
print("Encrypted Text:", encrypt_text(plain_text, key))

# Decryption
cipher_text = input("\nEnter message to decrypt: ")
key = int(input("Enter the key to decrypt: "))
print("\n--- Decryption ---")
print("Cipher Text   :", cipher_text)
print("Shift Pattern :", key)
print("Decrypted Text:", decrypt_text(cipher_text,key))

