# This function intends to encrypt plaintext using Rail Fence Ciphers

def RailFence_Encrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""
    for character in plainText:
        if not character.isalpha():
            plainText = plainText.replace(character, '')
    i = 0
    while i < int(key):
        temp = i
        while temp < len(plainText):
            cipher += plainText[temp].upper()
            temp += int(key)
        i += 1
    return cipher

while True:
    print("Ciphertext: " + RailFence_Encrypt() + '\n')
