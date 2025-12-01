ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptWithCaeser(plaintext, key):
            ciphertext = ""
            message = plaintext.replace(' ', '').upper()

            for char in message:
                print(char,end="")

                m_idx = ALPHABET.find(char)
                ciphertext += ALPHABET[(m_idx + key) % 26]

            return ciphertext

print('\n',f"Ciphertext : {encryptWithCaeser('hello my world', 3)}")
