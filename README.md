# SecurityTechnology_Note
This is a learning summary of the course EE4215 Security Technology, in City University of Hong Kong ~~and also a practice for markdown syntax~~.

Since it is just a short note and I intend not to make it so long, so some of the definition may not be perfect and just a short discription.
## The objectives of Computer Security (CIA)
### 1. Confidentiality (C)
>   Assures that private or confidential information is not made available or disclosed to unauthorized individuals
>
>   An example would be your gpa. Your scores should only be viewed by authorized parties such as professors

### 2. Integrity (I)
>   Assures that information and programs are changed only in a specified and authorized manner
>
>   For instance, the person who can change the password is only yourself. Keeeping Integrity means only the authorized person (that is you) to change the data

### 3. Availability (A)
>   Assures that systems work promptly and service is not denied to authorized users
>
>   Sometime if you hope to get a concert ticket online, you might find that the website is unacceptably slow and you (as an authorized entity) cannot access the website. This would mean the Availability is not maintained

## Terminology Explanation
### 1. Brute-Force Attack
>   Trying every possible key on a piece of ciphertext until an intelligible translation into plaintext is obtained.
>
>   See example on [Casear Cipher](https://github.com/kcwong395/SecurityTechnology_Note/blob/master/Classical%20Ciphers/Substitution/CaesarCipher/caesar_bruteForce.py) brute-force attempt

### 2. Cryptanalysis
>   Known as code-breaking, which is an attempt to deduce a specific plaintext or the key being used by studying the **nature** of the algorithm and some common **characteristics** of the plaintext.
>
>   For example, English Letter Frequencies:
>
>   Since letters are not equally distributed and letter E, T, A, etc are considered as very common letter in English. If encryption techniques such as Transposition or Substitution is highly conducted in the encryption algorithm, it would be a good approach to match the above letters to those letters with a high frequency in the ciphertext.

## Cipher
### 1. Symmetric Cipher Model
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

### 2. Classical Ciphers
>   The conversion from plaintext to ciphertext involve two methods, Substitution and Transposition
>
>   4.1 Substitution refers to substituting letters of the plaintext with other letters/symbol
>
>  - monoalphabetic is the unique mapping of plaintext alphabet to ciphertext alphabet such as [**Caesar Cipher**](https://github.com/kcwong395/SecurityTechnology_Note/tree/master/Classical%20Ciphers/Substitution/CaesarCipher), Hill, [**Playfair**](https://github.com/kcwong395/SecurityTechnology_Note/tree/master/Classical%20Ciphers/Substitution/PlayfairCipher)
>
>  - polyalphabetic means plaintext mapped to ciphertext based on key to select alphabet such as [**Vigenere**](https://github.com/kcwong395/SecurityTechnology_Note/tree/master/Classical%20Ciphers/Substitution/VigenereCipher), enigma
>
>  - stream means a keystream is generated for mapping plaintext to ciphertext such as one-time replaced
>
>
>   4.2 Transposition refers to rearranging plaintext (permutation)
>
>   [**Rail Fence Ciphers**](https://github.com/kcwong395/SecurityTechnology_Note/tree/master/Classical%20Ciphers/Transposition/RailFenceCipher)
>
>

### 3. Modern Encryption
>
