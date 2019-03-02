# This function intends to encrypt plaintext using playfair encryption method


def PlayfairEncrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""

    # table config
    table = []
    key = key.replace('J', 'I')
    key = key.upper()
    for character in key:
        if character not in table:
            table.append(character)
    for i in range(26):
        if chr(i + ord('A')) not in table and chr(i + ord('A')) != 'J':
            table.append(chr(i + ord('A')))
    # end of table config

    # plaintext config
    pair = 0
    for letter in plainText:
        if not letter.isalpha():
            plainText = plainText.replace(letter, "")
    plainText = plainText.upper()
    plainText = plainText.replace('J', 'I')
    while pair != len(plainText) // 2:
        if plainText[2 * pair] == plainText[2 * pair + 1]:
            plainText = plainText[:2 * pair + 1] + 'X' + plainText[2 * pair + 1:]
        pair += 1
    if len(plainText) % 2 == 1:
        plainText = plainText + 'X'
    # end of plaintext config

    # start encryption
    cpair = 0
    while cpair != len(plainText) // 2:
        rowA = table.index(plainText[2 * cpair]) // 5
        rowB = table.index(plainText[2 * cpair + 1]) // 5
        colA = table.index(plainText[2 * cpair]) % 5
        colB = table.index(plainText[2 * cpair + 1]) % 5
        if rowA == rowB:
            cipher += table[(table.index(plainText[2 * cpair]) + 1) % 5 + rowA * 5] + table[(table.index(plainText[2 * cpair + 1]) + 1) % 5 + rowB * 5]
        elif colA == colB:
            cipher += table[(table.index(plainText[2 * cpair]) + 5) % 25] + table[(table.index(plainText[2 * cpair + 1]) + 5) % 25]
        else:
            cipher += table[colB + rowA * 5] + table[colA + rowB * 5]
        cpair += 1
    # end of encryption
    return cipher


print("Ciphertext: " + PlayfairEncrypt())
a = input()
