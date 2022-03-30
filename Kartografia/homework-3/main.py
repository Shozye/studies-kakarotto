from Crypto.Cipher import ChaCha20
import json
from base64 import b64encode

def pad_with_zeroes(key: str) -> bytes:
    key_bytes = key.encode('utf-8')
    new_key = (32 - len(key_bytes)) * b'0' + key_bytes
    return new_key

plaintext = b"Attack on Titans" * 8  # 128 bytes
key = pad_with_zeroes("Mateusz")

cipher = ChaCha20.new(key=key)
bytes_ciphertext = cipher.encrypt(plaintext)

print("b64 encoded nonce and ciphertext")
nonce = b64encode(cipher.nonce).decode('utf-8')
ciphertext = b64encode(bytes_ciphertext).decode('utf-8')
print(json.dumps({"nonce": nonce, "ciphertext": ciphertext}, indent=4))


with open("ciphertext.bin", 'wb+') as file:
    file.write(bytes_ciphertext)

with open("nonce.bin", "wb+") as file:
    file.write(cipher.nonce)
