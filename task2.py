def simple_transposition_encrypt(text, key):
    columns = len(key)
    rows = len(text) // columns + (len(text) % columns != 0)
    matrix = [['' for _ in range(columns)] for _ in range(rows)]
    
    idx = 0
    for i in range(rows):
        for j in range(columns):
            if idx < len(text):
                matrix[i][j] = text[idx]
                idx += 1
    
    ciphertext = ''
    for j in range(columns):
        for i in range(rows):
            if matrix[i][j]:
                ciphertext += matrix[i][j]
    return ciphertext

def simple_transposition_decrypt(ciphertext, key):
    columns = len(key)
    rows = len(ciphertext) // columns + (len(ciphertext) % columns != 0)
    matrix = [['' for _ in range(columns)] for _ in range(rows)]
    
    idx = 0
    for j in range(columns):
        for i in range(rows):
            if idx < len(ciphertext):
                matrix[i][j] = ciphertext[idx]
                idx += 1

    plaintext = ''
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]:
                plaintext += matrix[i][j]
    return plaintext

with open("text.txt", "r") as text_file:
    text = text_file.read()
    key = "SECRET"
    
    encrypted_text = simple_transposition_encrypt(text, key)
    print("Зашифрований текст:", encrypted_text, "\n")

    decrypted_text = simple_transposition_decrypt(encrypted_text, key)
    print("Розшифрований текст:", decrypted_text)


def double_transposition_encrypt(text, key1, key2):
    first_encryption = simple_transposition_encrypt(text, key1)
    return simple_transposition_encrypt(first_encryption, key2)

def double_transposition_decrypt(ciphertext, key1, key2):
    first_decryption = simple_transposition_decrypt(ciphertext, key2)
    return simple_transposition_decrypt(first_decryption, key1)


with open("text.txt", "r") as text_file:
    text = text_file.read()
    key1 = "SECRET"
    key2 = "CRYPTO"
    
    encrypted_text = double_transposition_encrypt(text, key1, key2)
    print("Подвійно зашифрований текст:", encrypted_text, "\n")

    decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
    print("Розшифрований текст:", decrypted_text)