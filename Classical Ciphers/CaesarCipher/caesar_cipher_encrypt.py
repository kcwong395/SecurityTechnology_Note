# This function intends to encrypt plaintext using Caesar Cipher


def CaesareEncrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) + int(key) - ord('a')) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) + int(key) - ord('A')) % 26 + ord('A'))
        cipher += letter
    return cipher


print("Ciphertext: " + CaesareEncrypt())
a = input()
