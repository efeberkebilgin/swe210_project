from cryptography.fernet import Fernet
import hashlib
import base64


class EncryptionManager:

    def __init__(self, secret_key):


        # Generate SHA256 hash
        key = hashlib.sha256(secret_key.encode()).digest()

        # Convert to Fernet-compatible key
        self.fernet_key = base64.urlsafe_b64encode(key)

        # Fernet object
        self.cipher = Fernet(self.fernet_key)

    # ====================================
    # ENCRYPT DATA
    # ====================================
    def encrypt_data(self, plaintext):

        if not plaintext:
            return None

        encrypted = self.cipher.encrypt(
            plaintext.encode()
        )

        return encrypted.decode()

    # ====================================
    # DECRYPT DATA
    # ====================================
    def decrypt_data(self, encrypted_text):

        if not encrypted_text:
            return None

        decrypted = self.cipher.decrypt(
            encrypted_text.encode()
        )

        return decrypted.decode()