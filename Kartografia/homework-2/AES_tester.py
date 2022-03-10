from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import timeit


def measure_million_times_aes(key_length:int):
    starttime = timeit.default_timer()
    key = get_random_bytes(key_length)
    header = b'header'
    text = b"i want to cipher"
    for i in range(10000000):
        cipher = AES.new(key, AES.MODE_EAX)
        cipher.update(header)
        ciphertext, tag = cipher.encrypt_and_digest(text)
    return timeit.default_timer() - starttime

