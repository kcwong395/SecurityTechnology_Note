# SecurityTechnology_Note
This is a learning summary of the course EE4215 Security Technology, in City University of Hong Kong ~~and also a practice for markdown syntax~~.
## Terminology Explanation
### 1. Brute-Force Attack
>   Trying every possible key on a piece of cipher text until an intelligible translation into plain text is obtained.
>
>   See example on [Casear Cipher](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/CaesarCipher/caesar_cipher_BruteForce.py) brute-force attempt

### 2. Cryptanalysis
>   An attempt to deduce a specific plaintext or the key being used by studying the **nature** of the algorithm and some common **characteristics** of the plaintext. For example, English Letter Frequencies

### 3. Symmetric Cipher Model
>   Sender and recipient share a **common** secret key(K)
>
>   Mathematically,
>
>   C (Cipher text) = E<sub>k</sub>(P) where E is an encryption function
>
>   P (Plain text) = D<sub>k</sub>(C) where D is an decryption function
>
>   Problem:
>
>   Need a secure channel to distribute the common key

### 4. Classical Ciphers
>   The conversion from plain text to cipher text involve two methods, Substitution and Transposition
>
>   3.1 Substitution refers to substituting letters of the plain text with other letters/symbol
>
>  - monoalphabetic is the unique mapping of plaintext alphabet to ciphertext alphabet such as [**Caesar Cipher**](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/CaesarCipher/README.md), Hill, Playfair
>
>  - polyalphabetic means plaintext mapped to ciphertext based on key to select alphabet such as Vigenere, enigma
>
>  - stream means a keystream is generated for mapping plain text to cipher text such as one-time replaced
>
>
>   3.2 Transposition refers to rearranging plain text(permutation)
