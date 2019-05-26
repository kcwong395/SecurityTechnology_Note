# This function intends to encrypt plaintext with Vigenere Cipher


def VigenereEncrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""
    i = 0
    for letter in plainText:
        if 'a' <= letter <= 'z':
            if i >= len(key):
                i = 0
            letter = chr((ord(letter) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
            i += 1
        elif 'A' <= letter <= 'Z':
            if i >= len(key):
                i = 0
            letter = chr((ord(letter) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
            i += 1
        cipher += letter
    return cipher

while True:
    print("Ciphertext: " + VigenereEncrypt() + '\n')
