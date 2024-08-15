import os
import logging
from encryption.encryption_service import encrypt, decrypt

DOCUMENTS_DIR = "./encrypted_documents/"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_encrypted_document(file_content: bytes) -> str:
    encrypted_data = encrypt(file_content)
    file_id = os.urandom(16).hex()
    file_path = os.path.join(DOCUMENTS_DIR, f"{file_id}.enc")
    with open(file_path, "wb") as f:
        f.write(encrypted_data)
    logging.info(f"Document {file_id} encrypted and saved.")
    return file_path

def retrieve_decrypted_document(file_path: str) -> bytes:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        logging.info(f"Document decrypted from {file_path}.")
        return decrypt(encrypted_data)
    logging.warning(f"Document at {file_path} not found.")
    return None
