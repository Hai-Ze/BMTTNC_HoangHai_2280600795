import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import requests
from PyQt5 import QtWidgets
from ui.rsa_ui import Ui_Dialog  # Import giao diện từ file rsa_ui.py

class RSAWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(RSAWindow, self).__init__()
        self.setupUi(self)

        # Kết nối các nút bấm với hàm xử lý
        self.btn_generate.clicked.connect(self.generate_keys)
        self.bnt_encrypt.clicked.connect(self.encrypt_message)
        self.btn_decrypt.clicked.connect(self.decrypt_message)
        self.btn_sign.clicked.connect(self.sign_message)
        self.btn_verify.clicked.connect(self.verify_signature)

    def generate_keys(self):
        try:
            response = requests.get("http://localhost:5000/api/rsa/generate_keys")
            result = response.json()
            self.txt_information.setPlainText(result["message"])
        except Exception as e:
            self.txt_information.setPlainText(f"Lỗi: {str(e)}")

    def encrypt_message(self):
        try:
            message = self.txt_plain.toPlainText()
            data = {"message": message, "key_type": "public"}
            response = requests.post("http://localhost:5000/api/rsa/encrypt", json=data)
            result = response.json()
            if "encrypted_message" in result:
                self.txt_cipher.setPlainText(result["encrypted_message"])
                self.txt_information.setPlainText("Mã hóa thành công!")
                self.encrypted_message = result["encrypted_message"]
            else:
                self.txt_information.setPlainText(f"Lỗi: {result.get('error', 'Không rõ')}")
        except Exception as e:
            self.txt_information.setPlainText(f"Lỗi: {str(e)}")

    def decrypt_message(self):
        try:
            data = {"ciphertext": self.encrypted_message, "key_type": "private"}
            response = requests.post("http://localhost:5000/api/rsa/decrypt", json=data)
            result = response.json()
            if "decrypted_message" in result:
                self.txt_plain.setPlainText(result["decrypted_message"])
                self.txt_information.setPlainText("Giải mã thành công!")
            else:
                self.txt_information.setPlainText(f"Lỗi: {result.get('error', 'Không rõ')}")
        except Exception as e:
            self.txt_information.setPlainText(f"Lỗi: {str(e)}")

    def sign_message(self):
        try:
            message = self.txt_plain.toPlainText()
            data = {"message": message}
            response = requests.post("http://localhost:5000/api/rsa/sign", json=data)
            result = response.json()
            if "signature" in result:
                self.txt_signature.setPlainText(result["signature"])
                self.txt_information.setPlainText("Ký thành công!")
                self.signature = result["signature"]
            else:
                self.txt_information.setPlainText(f"Lỗi: {result.get('error', 'Không rõ')}")
        except Exception as e:
            self.txt_information.setPlainText(f"Lỗi: {str(e)}")

    def verify_signature(self):
        try:
            message = self.txt_plain.toPlainText()
            data = {"message": message, "signature": self.signature}
            response = requests.post("http://localhost:5000/api/rsa/verify", json=data)
            result = response.json()
            if "is_verified" in result:
                self.txt_information.setPlainText(f"Xác minh: {result['is_verified']}")
            else:
                self.txt_information.setPlainText(f"Lỗi: {result.get('error', 'Không rõ')}")
        except Exception as e:
            self.txt_information.setPlainText(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RSAWindow()
    window.show()
    sys.exit(app.exec_())