ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decryptWithCaeser(Cyphertext, key):
            plaintext = ""
            message = Cyphertext

            for char in message:
                print(char,end="")

                m_idx = ALPHABET.find(char)
                plaintext += ALPHABET[(m_idx - key) % 26]

            return plaintext

print('\n',f"Ciphertext : {decryptWithCaeser('KHOORPBZRUOG', 3)}")
