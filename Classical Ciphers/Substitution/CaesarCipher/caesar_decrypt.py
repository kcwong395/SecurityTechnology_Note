# This function intends to decrypt plaintext with a known key


def CaesarDecrypt():
    plainText = input("Cipher text: ")
    key = input("Key: ")
    cipher = ""
    for letter in plainText:
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - ord('a') - int(key)) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - ord('A') - int(key)) % 26 + ord('A'))
        cipher += letter
    return cipher

while True:
    print("Plaintext: " + CaesarDecrypt() + '\n')
