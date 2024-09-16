from task1 import vigenere_encrypt, vigenere_decrypt

def create_table(key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    for char in key.upper():
        if char not in table:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    return table

def table_encrypt(text, key, shift):
    table = create_table(key)
    ciphertext = []
    for char in text:
        if char.upper() in table:
            is_upper = char.isupper()
            idx = (table.index(char.upper()) + shift) % 26
            new_char = table[idx]
            ciphertext.append(new_char if is_upper else new_char.lower())
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def table_decrypt(ciphertext, key, shift):
    table = create_table(key)
    plaintext = []
    for char in ciphertext:
        if char.upper() in table:
            is_upper = char.isupper()
            idx = (table.index(char.upper()) - shift) % 26
            new_char = table[idx]
            plaintext.append(new_char if is_upper else new_char.lower())
        else:
            plaintext.append(char)
    return ''.join(plaintext)



with open("text.txt", "r") as text_file:
    text = text_file.read()
    key = "MATRIX"
    
    encrypted_text = table_encrypt(text, key, len(key))
    print("Зашифрований текст:", encrypted_text, "\n")

    decrypted_text = table_decrypt(encrypted_text, key, len(key))
    print("Розшифрований текст:", decrypted_text)


    encrypted_text = table_encrypt(vigenere_encrypt(text, key = "CRYPTOGRAPHY"), key = "CRYPTO", shift = 6)
    
    print("Зашифрований текст (шифр Віженера + табличний шифр):", encrypted_text, "\n")

    decrypted_text = vigenere_decrypt(table_decrypt(encrypted_text, key = "CRYPTO", shift = 6), key = "CRYPTOGRAPHY")

    print("Розшифрований текст:", decrypted_text)

    