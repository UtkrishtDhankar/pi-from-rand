import math
import random
import sys

usage_str = "Usage: python pi.py [number of pairs]"

def generate_pair(low = 1, high = 120):
    """
    Generates a pair of random integers between low and high.
    """

    a = random.randint(low, high)
    b = random.randint(low, high)

    return (a, b)


def main():
    if len(sys.argv) != 2:
        print(usage_str)
        return

    num_pairs = int(sys.argv[1])

    coprimes = 0
    for i in range(num_pairs):
        (a, b) = generate_pair()
        if math.gcd(a, b) == 1:
            coprimes += 1

    pi = math.sqrt(6 * num_pairs / coprimes)
    print(pi)

if __name__ == '__main__':
    main()
