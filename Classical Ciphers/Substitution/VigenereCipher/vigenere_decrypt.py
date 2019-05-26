# This function intends to decrypt Vigenere Ciphertext


def VigenereDecrypt():
    cipherText = input("Ciphertext: ")
    key = input("Key: ")
    plain = ""
    i = 0
    for letter in cipherText:
        if 'a' <= letter <= 'z':
            if i >= len(key):
                i = 0
            letter = chr((ord(letter) - ord(key[i])) % 26 + ord('a'))
            i += 1
        elif 'A' <= letter <= 'Z':
            if i >= len(key):
                i = 0
            letter = chr((ord(letter) - ord(key[i])) % 26 + ord('A'))
            i += 1
        plain += letter
    return plain

while True:
    print("Plaintext: " + VigenereDecrypt() + '\n')
