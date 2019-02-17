# This function intends to decrypt Caesar ciphertext by brute forcing all possible key

cipherText = input("Please enter the ciphertext to be decoded: \n")


def BruteForceAttack(cipherText):
    for key in range(26):
        for letter in cipherText:
            remain = ord(letter)
            if 'a' <= letter <= 'z':
                remain -= key
                if remain < ord('a'):
                    remain += 26
            elif 'A' <= letter <= 'Z':
                remain -= key
                if remain < ord('A'):
                    remain += 26
            print(chr(remain), end='')
        print()


print("\nThe following are all the possible plaintexts")
BruteForceAttack(cipherText)
a = input()
