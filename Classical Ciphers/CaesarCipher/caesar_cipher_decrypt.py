# This function intends to decrypt plaintext with a known key

plainText = input("Cipher text: \n")
key = input("Key: \n")


def CaesareEncrypt(plainText):
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - int(key) - ord('a')) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - int(key) - ord('A')) % 26 + ord('A'))
        cipher += letter
    return cipher


print("Plain text: ")
print(CaesareEncrypt(plainText))
a = input()
