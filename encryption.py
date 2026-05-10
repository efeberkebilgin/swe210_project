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
        Converts secret key into
        Fernet-compatible format.
        """

        # SHA256 HASH
        key = hashlib.sha256(
            secret_key.encode()
        ).digest()

        # BASE64 CONVERSION
        self.fernet_key = base64.urlsafe_b64encode(key)

        # FERNET OBJECT
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

        try:

            decrypted = self.cipher.decrypt(
                encrypted_text.encode()
            )

            return decrypted.decode()

        # HANDLE INVALID / CORRUPTED TOKENS
        except Exception:

            return None