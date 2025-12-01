# cropytography

## Caesar Cipher
The Caesar Cipher is one of the simplest and widely known encryption techniques.It is a monoalphabetic 
substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of 
positions down the alphabet.  

## How it works:
Shift (n): A fixed integer (key)determines the displacement.    
Encryption: E_n(x) = (x + n) \mod 26   
Decryption: D_n(x) = (x - n) \mod 26      
(Where x is the numerical index of the letter, i.e., A=0, B=1...)    


## Vigenère Cipher
The Vigenère Cipher is a polyalphabetic substitution cipher. Unlike Caesar, which uses a single 
shift value for the entire text, Vigenère uses a keyword to employ a series of different Caesar
ciphers based on the letters of that keyword.

## How it works:
Keyword: A word or phrase is repeated until it matches the length of the plaintext.  
Mechanism: Each letter of the plaintext is shifted by the corresponding letter of the keyword (where A=0, B=1, etc.).      
Encryption: C_i = (P_i + K_i) \mod 26   
Decryption: P_i = (C_i - K_i) \mod 26   
