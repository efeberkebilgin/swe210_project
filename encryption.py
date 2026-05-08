from cryptography.fernet import Fernet
import base64
import hashlib


# ====================================
# ENCRYPTION CLASS
# ====================================
class EncryptionManager:
    """
    Handles encryption and decryption
    using Fernet symmetric encryption.
    """

    def __init__(self, secret_key):
        """
        Converts app secret key into
        Fernet-compatible key.
        """

        # SHA256 hash
        key = hashlib.sha256(secret_key.encode()).digest()

        # Convert to base64
        self.fernet_key = base64.urlsafe_b64encode(key)

        # Fernet object
        self.cipher = Fernet(self.fernet_key)

    # =========================
    # ENCRYPT DATA
    # =========================
    def encrypt_data(self, plaintext):
        """
        Encrypts plaintext into secure token.
        """

        if not plaintext:
            return None

        encrypted = self.cipher.encrypt(plaintext.encode())

        return encrypted.decode()

    # =========================
    # DECRYPT DATA
    # =========================
    def decrypt_data(self, encrypted_text):
        """
        Decrypts encrypted token.
        """

        if not encrypted_text:
            return None

        decrypted = self.cipher.decrypt(encrypted_text.encode())

        return decrypted.decode()