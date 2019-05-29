# This function intends to extract the key given the plaintext and ciphertext


def CaesarKey():
    plainText = input("Plaintext: ")
    cipherText = input("Ciphertext: ")
    key = (ord(cipherText[0]) - ord(plainText[0])) % 26
    return key

while True:
    print("Key: " + str(CaesarKey()) + '\n')
