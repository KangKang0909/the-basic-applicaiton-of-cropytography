def encryptWithTransposition(plaintext, key):
    message = plaintext.replace(' ', '').upper()
    ciphertext = [''] * key
    #print(ciphertext)


    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
        #print(ciphertext)
    return ''.join(ciphertext)

print(f"Ciphertext : {encryptWithTransposition('hello world', 3)}")
