
import os
import hashlib
import secrets

class PasskeyManager:
    def __init__(self):
        self.passkeys = {}

    def generate_passkey(self, user_id):
        """Generate a secure passkey for a user."""
        key = secrets.token_urlsafe(32)
        hashed_key = hashlib.sha256(key.encode()).hexdigest()
        self.passkeys[user_id] = hashed_key
        return key

    def validate_passkey(self, user_id, passkey):
        """Validate a given passkey for a user."""
        hashed_key = hashlib.sha256(passkey.encode()).hexdigest()
        return self.passkeys.get(user_id) == hashed_key

if __name__ == "__main__":
    manager = PasskeyManager()
    user_id = "user123"
    key = manager.generate_passkey(user_id)
    print(f"Generated passkey for {user_id}: {key}")

    # Validate Passkey
    valid = manager.validate_passkey(user_id, key)
    print(f"Passkey validation result: {'Valid' if valid else 'Invalid'}")
