###  Playfair Cipher
>   Playfair Cipher, a **polyalphabetic cipher**, was invented by Charles Wheatstone in 1854, but named after his friend Baron Playfair. The idea of encryption algorithm is to **substitude multiple letters**.

**Demostration:**
>
>   Message: Hey! Meet me after the lecture.
>
>   Key: playfair

>   Table Config
>
>   Prepare a 5 x 5 matrix and fill the key in the table
>
>   | P | L | A | Y | F |
>   |---|---|---|---|---|
>   | **I** | **R** |   |   |   |
>   |   |   |   |   |   |
>   |   |   |   |   |   |
>   |   |   |   |   |   |   |
>
>   Noted that if the letter is already in the table, just do nothing with the repeated one. In this case, A only appears once
>
>   **I and J share the same box so the number of letters is limited to 25**
>
>   Fill in the table with the remaining letters in alphabetical order
>
>   | P | L | A | Y | F |
>   |---|---|---|---|---|
>   | **I** | **R** | **B** | **C** | **D** |
>   | **E** | **G** | **H** | **K** | **M** |
>   | **N** | **O** | **Q** | **S** | **T** |
>   | **U** | **V** | **W** | **X** | **Z** |

>   Plaintext Config
>
>   Before we start to encrypt the plaintext, there are a few rules we need to follow:
>
>   1. Replace J with I
>
>   2. Separate the plaintext in pairs, ignore the non-alphabetic character
>
>   He yM ee tm ea ft er th el ec tu re
>
>   3. Add a X in between a pair if both characters are the same
>
>   He yM eX et me af te rt he le ct ur e
>
>   4. Add a X at the end of the plaintext if the last element is not yet paired up (odd)
>
>   He yM eX et me af te rt he le ct ur eX

>   Start Encryption
>
>   Look for the location of each pair in the table
>
>   - if they are in the same row, right shift the pairs, eg, He -> KG
>
>   - if they are in the same column, downward shift the pairs, eg, PI -> IE (just an example, this is not in this plaintext)
>
>   - if they are neither in the same row nor in the same column, the cipher will be the two characters which can form a rectangle with that pair, eg, eX -> KU

>   Result: KGFKKUMNEGYPNMDOKGPGDSVIKU
