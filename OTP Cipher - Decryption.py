ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptWithOTP(Ciphertext, key):
    key = key.replace(' ', '').upper()
    message = Ciphertext.replace(' ', '').upper()

    if len(key) < len(message):
        exit("try longer key")

    ciphertext = ""

    for i in range(len(message)):
        m_idx = ALPHABET.find(message[i])
        k_idx = ALPHABET.find(key[i])
        ciphertext += ALPHABET[(m_idx - k_idx) % 26]
    return ciphertext

print(f"Ciphertext : {encryptWithOTP('NOYQQZUAUA', 'gknfcdgjjx')}")

