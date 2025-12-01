# cropytography

## Caesar Cipher
The Caesar Cipher is one of the simplest and widely known encryption techniques.It is a monoalphabetic 
substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of 
positions down the alphabet.
### How it works:
Shift (n): A fixed integer (key)determines the displacement.    
Encryption: C = (P + k) mod 26   
Decryption: P = (C − k) mod 26      
(Where x is the numerical index of the letter, i.e., A=0, B=1...)    


## Vigenère Cipher
The Vigenère Cipher is a polyalphabetic substitution cipher. Unlike Caesar, which uses a single 
shift value for the entire text, Vigenère uses a keyword to employ a series of different Caesar
ciphers based on the letters of that keyword.
### How it works:
Keyword: A word or phrase is repeated until it matches the length of the plaintext.  
Mechanism: Each letter of the plaintext is shifted by the corresponding letter of the keyword (where A=0, B=1, etc.).      
Encryption: C = (P + K) \mod 26   
Decryption: P = (C - K) \mod 26   


## one-time pad
The One-Time Pad (OTP) is a theoretically unbreakable encryption technique. It is a substitution cipher where the key is a random string of characters that is at least as long as the plaintext and is used only once.
### how it works
Its working principle of Decryption and Encryption is identical with Vigenère Cipher. the only thing is that the key should be as the same length as the plaintext.  
Encryption: C = (P + K) \mod 26     
Decryption: P = (C - K) \mod 26     


## summary
Three are Substitution Ciphers that rely on the same fundamental logic: shifting the plaintext letter by a certain value modulo 26.  
The only difference is how the shift value (K) is determined for each letter.  
### key Takeaway:
Caesar is a Vigenère cipher with a keyword length of 1.   
Vigenère is a One-Time Pad with a repeating, non-random key.   
OTP is the "perfect" version where the key never repeats and is truly random.   


## Transposition Cipher
The Transposition Cipher is a cryptographic technique that rearranges the positions of the characters in the plaintext without changing the characters themselves. Unlike the One-Time Pad (which is a Substitution cipher), this is a Permutation technique.    
### How it works
The code you provided implements a Columnar Transposition (specifically similar to a Rail Fence pattern). It writes the message out effectively in rows but reads them out in columns based on the key.
this relies on index hopping:
1. Index Selection: You select characters at indices:i, i+k, i+2k, ...  
2. Concatenation: You do this for every starting column from 0 to k-1.
