from flask import Flask, render_template, request, send_from_directory
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.raifence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Route cho favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Routes cho Caesar cipher
@app.route('/caesar.html')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f'text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}'

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f'text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}'

# Routes cho Vigenere cipher
@app.route('/vigenere.html')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}'

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}'

# Routes cho Playfair cipher
@app.route('/playfair.html')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKey']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    matrix_display = "<table border='1' style='border-collapse: collapse; margin: 20px auto;'>"
    for row in matrix:
        matrix_display += "<tr>"
        for cell in row:
            matrix_display += f"<td style='padding: 10px; text-align: center; width: 40px; height: 40px;'>{cell}</td>"
        matrix_display += "</tr>"
    matrix_display += "</table>"
    return f'Key: {key}<br/>Playfair Matrix:<br/>{matrix_display}'

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f'text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}'

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f'text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}'

# Routes cho Railfence cipher
@app.route('/railfence.html')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}'

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}'

# Routes cho Transposition cipher
@app.route('/transposition.html')
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}'

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    return f'text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}'

# Hàm main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)