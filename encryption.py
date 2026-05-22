import base64
import hashlib
from cryptography.fernet import Fernet


class EncryptionManager:
    """Encrypts and decrypts sensitive data with Fernet symmetric encryption."""

    def __init__(self, secret_key):
        if not secret_key:
            raise ValueError("ENCRYPTION_SECRET_KEY cannot be empty.")

        key = hashlib.sha256(secret_key.encode("utf-8")).digest()
        self.fernet_key = base64.urlsafe_b64encode(key)
        self.cipher = Fernet(self.fernet_key)

    def encrypt_data(self, plaintext):
        if plaintext is None or plaintext == "":
            return None

        encrypted = self.cipher.encrypt(plaintext.encode("utf-8"))
        return encrypted.decode("utf-8")

    def decrypt_data(self, encrypted_text):
        if encrypted_text is None or encrypted_text == "":
            return None

        try:
            decrypted = self.cipher.decrypt(encrypted_text.encode("utf-8"))
            return decrypted.decode("utf-8")
        except Exception:
            return "[Decryption failed]"
