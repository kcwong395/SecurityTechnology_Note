# SecurityTechnology_Note
This is a learning summary of the course EE4215 Security Technology
## Terminology Explanation
### 1. Brute-Force Attack
>   Trying every possible key on a piece of cipher text until an intelligible translation into plain text is obtained.

### 2. Cryptanalysis
>   An attempt to deduce a specific plaintext or the key being used by studying the **nature** of the algorithm and some common **characteristics** of the plaintext

### 3. Symmetric Cipher Model
>   Sender and recipient share a common secret key(k)
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
>  - monoalphabetic is the unique mapping of plaintext alphabet to ciphertext alphabet such as [Caesar](Classical-Cipher/CaesarCipher/README.md), Hill, Playfair
>
>  - polyalphabetic means plaintext mapped to ciphertext based on key to select alphabet such as Vigenere, enigma
>
>  - stream means a keystream is generated for mapping plain text to cipher text such as one-time replaced
>
>
>   3.2 Transposition refers to rearranging plain text(permutation)
<<<<<<< HEAD
=======
## Encryption Method
### 1. G.C.D.
>   G.C.D. stands for the Greatest Common Divisor. gcd(a, b) is the greatest number which divides a and b. This is important for us to look into as it is helpful in some encryption methods such as RSA.

### 2. Symmetric Cipher Model
>>>>>>> bd306ea1936ddc264ebf101be3b813e40bfdd63d
