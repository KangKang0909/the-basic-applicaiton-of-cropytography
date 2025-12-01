def decryptWithTransposition(ciphertext, key):
    base_rows = len(ciphertext) // key
    remainder = len(ciphertext) % key

    grid = [''] * key
    current_idx = 0

    for col in range(key):
        size = base_rows + 1  if col < remainder else base_rows
        grid[col] = ciphertext[current_idx: current_idx + size]
        current_idx += size


    plaintext = []
    num_rows = base_rows + 1 if remainder else base_rows

    for r in range(num_rows):
        for c in range(key):
            # Only append if this column actually has a character at this row
            if r < len(grid[c]):
                plaintext.append(grid[c][r])

    return ''.join(plaintext)


print(f"Plaintext : {decryptWithTransposition('HLOLEORDLWL', 3)}")