import math
import random
import sys
import argparse


def generate_pair(low = 1, high = 120):
    """
    Generates a pair of random integers between low and high.
    """

    a = random.randint(low, high)
    b = random.randint(low, high)

    return (a, b)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pairs",
                        help="the number of pairs generated",
                        type=int, default=1000)
    parser.add_argument("-m", "--max",
                        help="the max random number possible",
                        type=int,
                        default=120)
    args = parser.parse_args()

    num_pairs = args.pairs

    coprimes = 0
    for i in range(num_pairs):
        (a, b) = generate_pair(1, args.max)
        if math.gcd(a, b) == 1:
            coprimes += 1

    pi = math.sqrt(6 * num_pairs / coprimes)
    print(pi)

if __name__ == '__main__':
    main()
