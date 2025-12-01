ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptWithVignere(plaintext, key):

    key = key.replace(' ', '').upper()
    message = plaintext.replace(' ', '').upper()

    ciphertext = ""

    for i in range(len(message)):
        m_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i % len(key)])
        ciphertext += ALPHABET[(m_idx + k_idx) % 26]

    return ciphertext


plaintext=input('please input your plaintext:')
key=input('please input your plaintext:')

print(f"Ciphertext : {encryptWithVignere(plaintext, key)}")

