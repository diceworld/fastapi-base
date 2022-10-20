import hashlib


class HashHelper:
    @staticmethod
    def encode(plaintext: str) -> str:
        m = hashlib.sha256()
        m.update(plaintext.encode('utf-8'))

        ciphertext = m.hexdigest()
        return ciphertext
