# This function intends to encrypt plaintext using playfair encryption method


def PlayfairEncrypt():
    plainText = input("Plaintext: ")
    key = input("Key: ")
    cipher = ""

    # table config
    alphaTable = []
    table = []
    for i in range(26):
        alphaTable.append(chr(i + ord('a')))
    for character in key:
        if character in alphaTable:
            if character == 'i' or character == 'j':
                alphaTable.pop(alphaTable.index('i'))
                alphaTable.pop(alphaTable.index('j'))
                table.append('i')
            else:
                alphaTable.pop(alphaTable.index(character))
                table.append(character)
    for letter in alphaTable:
        table.append(letter)
    for i in range(5):
        print(table[i * 5: (i+1) * 5])
    # end of table config

    # plaintext config
    pair = 0
    plainText = plainText.lower()
    plainText = plainText.replace(" ", "")
    while pair != len(plainText) // 2:
        if plainText[2 * pair] == 'j':
            plainText[2 * pair] = 'i'
        elif plainText[2 * pair + 1] == 'j':
            plainText[2 * pair + 1] = 'i'
        if plainText[2 * pair] == plainText[2 * pair + 1]:
            plainText = plainText[:2 * pair + 1] + 'x' + plainText[2 * pair + 1:]
        pair += 1
    if len(plainText) % 2 == 1:
        plainText = plainText + 'x'
    print(plainText)
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
            idA = table.index(plainText[2 * cpair]) + 5
            if idA > 24:
                idA = idA - 20
            idB = table.index(plainText[2 * cpair + 1]) + 5
            if idB > 24:
                idB = idB - 20
            cipher += table[idA] + table[idB]
        else:
            cipher += table[colB + rowA * 5] + table[colA + rowB * 5]
        cpair += 1
    # end of encryption
    return cipher


print("Ciphertext: " + PlayfairEncrypt())
a = input()
