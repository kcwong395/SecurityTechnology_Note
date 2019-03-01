# This function intends to decrypt plaintext with a known key


def CaesareEncrypt():
    plainText = input("Cipher text: ")
    key = input("Key: ")
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - int(key) - ord('a')) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - int(key) - ord('A')) % 26 + ord('A'))
        cipher += letter
    return cipher


print("Plaintext: " + CaesareEncrypt())
a = input()
