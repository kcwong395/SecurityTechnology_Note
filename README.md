# SecurityTechnology_Note
This is a learning summary of the course EE4215 Security Technology, in City University of Hong Kong ~~and also a practice for markdown syntax~~.
## Terminology Explanation
### 1. Brute-Force Attack
>   Trying every possible key on a piece of ciphertext until an intelligible translation into plaintext is obtained.
>
>   See example on [Casear Cipher](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/CaesarCipher/caesar_bruteForce.py) brute-force attempt

### 2. Cryptanalysis
>   Known as code-breaking, which is an attempt to deduce a specific plaintext or the key being used by studying the **nature** of the algorithm and some common **characteristics** of the plaintext.
>
>   For example, English Letter Frequencies:
>
>   Since letters are not equally distributed and letter E, T, A, etc are considered as very common letter in English. If encryption techniques such as Transposition or Substitution is highly conducted in the encryption algorithm, it would be a good approach to match the above letters to those letters with a high frequency in the ciphertext.

### 3. Symmetric Cipher Model
>   Sender and recipient share a **common** secret key(K)
>
>   Mathematically,
>
>   C (Ciphertext) = E<sub>k</sub>(P) where E is an encryption function
>
>   P (Plaintext) = D<sub>k</sub>(C) where D is an decryption function
>
>   Problem:
>
>   Need a **secure channel** to distribute the common key otherwise the key might be exposed under the risk of interception.

### 4. Classical Ciphers
>   The conversion from plaintext to ciphertext involve two methods, Substitution and Transposition
>
>   4.1 Substitution refers to substituting letters of the plaintext with other letters/symbol
>
>  - monoalphabetic is the unique mapping of plaintext alphabet to ciphertext alphabet such as [**Caesar Cipher**](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/CaesarCipher/README.md), Hill, [**Playfair**](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/PlayFairCipher/README.md)
>
>  - polyalphabetic means plaintext mapped to ciphertext based on key to select alphabet such as Vigenere, enigma
>
>  - stream means a keystream is generated for mapping plaintext to ciphertext such as one-time replaced
>
>
>   4.2 Transposition refers to rearranging plaintext(permutation)
>
