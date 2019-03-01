###  Playfair Cipher
>   Playfair Cipher, a **polyalphabetic cipher**, was invented by Charles Wheatstone in 1854, but named after his friend Baron Playfair. The idea of encryption algorithm is to **substitude multiple letters**.

**Demostration:**
>
>   Message: I came, I saw, I conquered
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
>   Fill in the table with the remaining letter in alphabetical order
>
>   | P | L | A | Y | F |
>   |---|---|---|---|---|
>   | **I** | **R** | **B** | **C** | **D** |
>   | **E** | **G** | **H** | **K** | **M** |
>   | **N** | **O** | **Q** | **S** | **T** |
>   | **U** | **V** | **W** | **X** | **Z** |
>
>
>
>   Result: Q kium, Q aie, Q kwvycmzml
