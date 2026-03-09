from cryptography.fernet import Fernet
import hmac
import hashlib
import os

# Key file for persistence
key_file = 'encryption_key.key'

# Load or generate key
if os.path.exists(key_file):
    with open(key_file, 'rb') as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)

cipher_suite = Fernet(key)

# Encrypt a sensitive file
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File {file_path} encrypted successfully.")
# Decrypt the encrypted file
def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {original_file_path} decrypted successfully.")

def constant_time_compare(val1, val2):
    return hmac.compare_digest(val1, val2)

# Encrypt the sensitive data file first
encrypt_file('sensitive-data.txt')

# Example usage
user_input = input('Enter your password: ')

# Compute the SHA-256 hash of the correct password ('password123')
stored_hash = hashlib.sha256('password123'.encode()).hexdigest()

# Compute the SHA-256 hash of the user's input
user_input_hash = hashlib.sha256(user_input.encode()).hexdigest()

# Compare the stored hash with the user's input hash using constant-time comparison
if constant_time_compare(stored_hash, user_input_hash):
    # If the hashes match, authentication is successful
    print("Authentication successful.")
    # Only decrypt if authenticated
    decrypt_file('sensitive-data.txt.enc')
else:
    # If the hashes do not match, authentication fails
    print("Authentication failed.")