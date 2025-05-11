import math
import random
from datetime import datetime
import sys

# Collatz function
def coll(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

# Seed RNG with current timestamp
random.seed(datetime.now().timestamp())

# Config
LOWER_BOUND = 5764000000000000000
UPPER_BOUND = 10 ** 32
STEP_LIMIT = 10 ** 6
PROGRESS_EVERY = 10**5  # print progress every N trials

nofN = 0

while True:
    nofN += 1

    # Generate large random number
    N = random.randrange(LOWER_BOUND, UPPER_BOUND)
    original_N = N
    counter = 0
    max_val = N

    # Run Collatz steps
    while True:
        N = coll(N)
        counter += 1
        if N > max_val:
            max_val = N
        if N < LOWER_BOUND:
            break
        if counter > STEP_LIMIT:
            print('\n\nPOSSIBLE SOLUTION FOUND:')
            print(f'Original N: {original_N}')
            print(f'Final N: {math.floor(N)}')
            print(f'Steps: {counter}')
            print(f'Max value reached: {max_val}\n')
            with open('possible_solutions.txt', 'a') as f:
                f.write(f'{original_N}\n')
            sys.exit()

    # Print periodic progress
    if nofN % PROGRESS_EVERY == 0:
        print(f'Checked {nofN:,} numbers... Last: {original_N}, Steps: {counter}, Max: {max_val}')

