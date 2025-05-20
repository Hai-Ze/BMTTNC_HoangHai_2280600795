class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypt_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypt_text += text[pointer]
                pointer += key
        return encrypt_text
    def decrypt(self, text, key):
        decrypt_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypt_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypt_text) 