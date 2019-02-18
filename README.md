# SecurityTechnology_Note
This is a learning summary of the course EE4215 Security Technology
## Terminology Explanation
* ### Brute-Force Attack
>   Trying every possible key on a piece of ciphertext until an intelligible translation into plaintext is obtained.
## Encryption Method

* ### G.C.D.
>   G.C.D. stands for the Greatest Common Divisor. gcd(a, b) is the greatest number which divides a and b. This is important for us to look into as it is helpful in some encryption methods such as RSA.

* ### Caesar Cipher
>   Caesar Cipher, named after Julius Caesar, is a type of **substitution** cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

    **Demostration:**

    Message: abc

    Key: 3

    Result: def

    **Algorithm:**

    E<sub>n</sub>(x)=(x+n) mod 26

    D<sub>n</sub>(x)=(x-n) mod 26
