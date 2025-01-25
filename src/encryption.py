from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_text(self, text):
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt_text(self, encrypted_text):
        return self.cipher.decrypt(encrypted_text.encode()).decode()

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
