def extend_key(text, key):
    key = list(key.upper())
    if len(text) == len(key):
        return ''.join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(plaintext, key):
    key = extend_key(plaintext, key)
    ciphertext = []
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(new_char)
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = extend_key(ciphertext, key)
    plaintext = []
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(new_char)
        else:
            plaintext.append(char)

    return ''.join(plaintext)




with open("text.txt", "r") as text_file:

    text = text_file.read()
    key = "CRYPTOGRAPHY"
    
    encrypted_text = vigenere_encrypt(text, key)
    print("Зашифрований текст:", encrypted_text, "\n")

    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Розшифрований текст:", decrypted_text)
