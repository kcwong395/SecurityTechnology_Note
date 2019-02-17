# This function intends to encrypt plaintext using Caesar Cipher

plainText = input("Please enter the plaintext to be encoded: \n")
key = input("Please enter the key for encryption: \n")


def CaesareEncrypt(plainText):
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) + int(key) - ord('a')) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) + int(key) - ord('A')) % 26 + ord('A'))
        cipher += letter
    return cipher

print("The following is the encrypted message: ")
print(CaesareEncrypt(plainText))
a = input()
