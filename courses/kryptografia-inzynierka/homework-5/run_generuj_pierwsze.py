from generuj_pierwsze import main
from tqdm import tqdm
import time

if __name__ == "__main__":
    bits_needed = [128, 256, 512, 1024, 1536, 2048, 3072, 4096]
    for amount_of_bits in tqdm(bits_needed, "Creating prime data..."):
        start = time.time()
        main(amount_of_bits)
        print(f"Took {round(time.time()- start)} seconds")
