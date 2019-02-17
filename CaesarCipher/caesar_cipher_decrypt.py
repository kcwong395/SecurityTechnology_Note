# This function intends to decrypt plaintext with a known key

plainText = input("Please enter the ciphertext to be decoded: \n")
key = input("Please enter the key for decryption: \n")


def CaesareEncrypt(plainText):
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - int(key) - ord('a')) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - int(key) - ord('A')) % 26 + ord('A'))
        cipher += letter
    return cipher


print("The following is the decrypted message: ")
print(CaesareEncrypt(plainText))
a = input()
