ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decryptWithVignere(ciphertext, key):

    key = key.replace(' ', '').upper()
    message = ciphertext.replace(' ', '').upper()

    plaintext = ""

    for i in range(len(message)):
        c_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i % len(key)])
        plaintext += ALPHABET[(c_idx - k_idx) % 26]

    return plaintext



print(f"Plaintext : {decryptWithVignere('LXFOPVEFRNHR', 'lemon')}")
