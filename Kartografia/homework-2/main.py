from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import timeit


def estimate_time_needed_to_bruteforce_key(length: int, am_per_second: int):
    am_keys = 2 ** length
    time_needed_s = (am_keys / am_per_second) // 2  # we should find it halfway
    return time_needed_s


def measure_million_times_aes(key_length: int):
    start_time = timeit.default_timer()
    key = get_random_bytes(key_length)
    header = b'header'
    text = b"i want to cipher"
    TIMES = 5000
    for i in range(TIMES):
        cipher = AES.new(key, AES.MODE_EAX)
        cipher.update(header)
        ciphertext, tag = cipher.encrypt_and_digest(text)
    MILLION = 1000000
    time_needed_for_million = int((timeit.default_timer() - start_time) * (MILLION / TIMES))
    amount_in_second = int(MILLION * 1/time_needed_for_million)
    return amount_in_second


def main():
    lengths = [40, 56, 90, 128, 256]
    pad = 40
    print("Times to bruteforce key of some length in seconds")
    print("on my pc calculated with 16bit key")
    print("Key Length".ljust(pad), "time 10**6".ljust(pad), "time MyPC".ljust(pad), "PLNs".ljust(pad))
    for length in lengths:
        key_len = length
        encryptions10to6 = estimate_time_needed_to_bruteforce_key(length, 1000000)
        my_pc_encryptions = estimate_time_needed_to_bruteforce_key(length, measure_million_times_aes(16))
        kwhprice = 0.64
        powerusagekwh = 0.5
        PLNs = str((my_pc_encryptions / 3600) * powerusagekwh * kwhprice)
        print(str(key_len).ljust(pad), str(encryptions10to6).ljust(pad), str(my_pc_encryptions).ljust(pad),
              str(PLNs).ljust(pad))


if __name__ == "__main__":
    main()
