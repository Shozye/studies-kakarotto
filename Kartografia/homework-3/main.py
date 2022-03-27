from Crypto.Cipher import ChaCha20

plaintext = b"Attack at dawnnn"*8 # 128 bytes
my_name = "Mateusz"
key = (my_name+"0"*(32-len(my_name))).encode('utf-8') # it just pads the key to 32 bytes
print(f"key={key}\nplaintext={plaintext}")
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext)

print(f"ciphertext={ciphertext}")

with open("my_output.bin", 'wb+') as file:
    file.write(ciphertext)
