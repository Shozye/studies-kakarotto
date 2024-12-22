import sys
import os
import math
import random
import json

# CREDITS : https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
                149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                307, 311, 313, 317, 331, 337, 347, 349]


def get_random(amount_of_bits: int):
    return random.randrange(2 ** (amount_of_bits - 1) + 1, 2 ** amount_of_bits - 1)


def get_lower_prime(amount_of_bits: int):
    """Generate a prime candidate divisible primes from FIRST_PRIMES list"""
    while True:
        prime_candidate = get_random(amount_of_bits)
        for divisor in FIRST_PRIMES:
            if prime_candidate % divisor == 0 and divisor ** 2 <= prime_candidate:
                break
        else:
            return prime_candidate


def is_miller_rabin_passed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    # kiedys to napisalem sam ale teraz to zerżnałem.
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def get_prime(amount_of_bits: int):
    while True:
        prime_candidate = get_lower_prime(amount_of_bits)
        if not is_miller_rabin_passed(prime_candidate):
            continue
        else:
            return prime_candidate


def main(amount_of_bits: int):
    # Tworzymy folder do ktorego bedziemy wrzucac wygenerowane liczby pierwsze
    primes_to_generate = 50
    e = 65537

    primes = list()
    while primes_to_generate != 0:
        prime = get_prime(amount_of_bits)
        if math.gcd(prime, e) == 1:
            primes.append(prime)
            primes_to_generate -= 1

    DATA_FILENAME = "primes_data"
    path_to_data_folder = os.path.join(os.getcwd(), DATA_FILENAME)
    if not os.path.isdir(path_to_data_folder):
        os.mkdir(path_to_data_folder)

    filename = f"p_{amount_of_bits}.txt"
    path_to_file = os.path.join(DATA_FILENAME, filename)

    with open(path_to_file, 'w+') as file:
        file.write("\n".join(list(map(str, primes))))


def print_usage():
    print("""Usage:
    python3 generuj_pierwsze.py <amount_of_bits>""")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    main(int(sys.argv[1]))
