<h1 style="text-align: center; color: lightcoral"> Cryptography </h1>

## the basic principle
### Caesar Cipher
The Caesar Cipher is one of the simplest and widely known encryption techniques.It is a monoalphabetic 
substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of 
positions down the alphabet.
### How it works:
Shift (n): A fixed integer (key)determines the displacement.    
[Encryption: C = (P + k) mod 26](Caesar%20Cipher%20-%20Encryption.py)   
[Decryption: P = (C − k) mod 26](Caesar%20Cipher%20-%20Decryption.py)     
(Where x is the numerical index of the letter, i.e., A=0, B=1...)    


### Vigenère Cipher
The Vigenère Cipher is a polyalphabetic substitution cipher. Unlike Caesar, which uses a single 
shift value for the entire text, Vigenère uses a keyword to employ a series of different Caesar
ciphers based on the letters of that keyword.
### How it works:
Keyword: A word or phrase is repeated until it matches the length of the plaintext.  
Mechanism: Each letter of the plaintext is shifted by the corresponding letter of the keyword (where A=0, B=1, etc.).      
[Encryption: C = (P + K) \mod 26](Vigenere%20Cipher%20-%20Encryption.py)     
[Decryption: P = (C - K) \mod 26](Vigenere%20Cipher%20-%20Decryption.py)    


### one-time pad
The One-Time Pad (OTP) is a theoretically unbreakable encryption technique. It is a substitution cipher where the key is a random string of characters that is at least as long as the plaintext and is used only once.
### how it works
Its working principle of Decryption and Encryption is identical with Vigenère Cipher. the only thing is that the key should be as the same length as the plaintext.  
[Encryption: C = (P + K) \mod 26](OTP%20Cipher%20-%20Encryption.py)      
[Decryption: P = (C - K) \mod 26](OTP%20Cipher%20-%20Decryption.py)      


### summary
Three are Substitution Ciphers that rely on the same fundamental logic: shifting the plaintext letter by a certain value modulo 26.  
The only difference is how the shift value (K) is determined for each letter.  
### key Takeaway:
Caesar is a Vigenère cipher with a keyword length of 1.   
Vigenère is a One-Time Pad with a repeating, non-random key.   
OTP is the "perfect" version where the key never repeats and is truly random.   


### Transposition Cipher
The Transposition Cipher is a cryptographic technique that rearranges the positions of the characters in the plaintext without changing the characters themselves. Unlike the One-Time Pad (which is a Substitution cipher), this is a Permutation technique.    
### How it works
The code you provided implements a Columnar Transposition (specifically similar to a Rail Fence pattern). It writes the message out effectively in rows but reads them out in columns based on the key.
this relies on index hopping:
1. Index Selection: You select characters at indices:i, i+k, i+2k, ...  
2. Concatenation: You do this for every starting column from 0 to k-1.


## security key cryptography 



## public key cryptography
RSA encryption is, in fact, almost completely obsolete, but RSA is one of the classic asymmetric algorithms and does a good job.
This concept will be helpful when learning about more modern approaches.

### [RSA Key Generation](RSA%20Key%20Generation.py)
1. Generate a large number, n:    
• Select two large prime numbers, p and q, so that n = pq.   
• The number n should be large, typically a minimum of 512 bits.   
2. Form the public key:  
• Find a number, e, such that [1 < e < (p − 1)(q − 1)].   
• The values e and (p − 1)(q − 1) must be coprime; no common factor for e and (p − 1)(q − 1), except for 1.   
• [Using the codes to look for the co-primes between both.](Find%20Co-primes.py)   
• The public key is the pair (n, e).   
3. Generate the private key:   
• A number, d, is calculated from p, q, and e such as.   
• The number d is the inverse of [e mod (p − 1)(q − 1)].   
• [Using the Extended Euclidean algorithm to look for the inverse](Extended%20Euclidean%20Algorithm.py)      
• The private key is the pair (n, d).   

### [RSA – Encryption/Decryption](RSA_En_De.py)  
To encrypt the a plaintext message P, using the public key (n, e), the sender uses the formula   
C = P<sup>e</sup> mod n  
To decrypt the ciphertext, C, the receiver uses the private key, d, and the formula:  
P = C<sup>d</sup> mod n

### Digital Signature Standard
Digital signature infrastructures have three distinct goals:   
Authenticity: It verifies that the signer is who they say they are. It confirms the source of the message.   
Integrity: It proves that the contents of the message have not been altered or modified in transit. If even one bit of data is changed, the signature becomes invalid.   
Non-Repudiation: It ensures the signer cannot deny signing the document later. Because the signature is unique to both the document and the signer's private key, it serves as legally binding proof of origin   

Digital signatures work as follows:
• If Alice wants to digitally sign a message to Bob, she performs the following actions:   
– Alice generates a message digest of the original plain-text message using one of the cryptographically sound hashing algorithms, such as SHA-1.    
– Alice then encrypts only the message digest using her private key. This encrypted message digest is the digital signature.    
– Alice appends the signed message digest to the plain-text message.   
– Alice transmits the appended message to Bob.   

• When Bob receives the digitally signed message, he reverses the procedure, as follows:  
– Bob decrypts the digital signature using Alice’s public key.  
– Bob uses the same hashing function to create a message digest of the full plain-text message received from Alice.   
– Bob then compares the decrypted message digest he received from Alice with the message digest he computed himself.    
– If the two digests match, he can be assured that the message he received was sent by Alice. If they do not match, either the message was not sent by Alice or the message was modified while in transit.   

### [Diffie-Hellman Algorithm](Diffie-Hellman-Algorithm.py)
Algorithm details:  
1. Alice picks numbers p and g, where p is a large prime and g is a number less than p, Alice could send the numbers (publicly) to Bob.   
2. Both Alice and Bob choose (separately) a 512-bit number at random and keeps it secret. Alice’s number is S<sub>A</sub>, and Bob’s number is $S_B$.   
3. Alice computes $(T_A = g^{S_A} \mod p)$. Bob computes $(T_B = g^{S_B} \mod p)$. 
4. Alice and Bob exchange their numbers (in either order): $T A \Leftrightarrow T B$    
5. Alice computes $(K = T_B^{S_A} \mod p)$. Bob computes $(K = T_A^{S_B} \mod p)$. The result will be the same number, $K$. That is because:$$T_B^{S_A} = (g^{S_B})^{S_A} = g^{(S_B S_A)} = g^{(S_A S_B)} = (g^{S_A})^{S_B} = T_A^{S_B} \mod p$$  

