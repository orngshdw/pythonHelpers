import itertools
import logging
import string

from time import time


def setup_logging():
    logging.basicConfig(format='%(message)s', level=logging.INFO)


def guess(string_of_characters, guess_length):
    for word in itertools.product(string_of_characters, repeat=guess_length):
        skip = True if len(set(word)) < 5 else False
        if skip:
            continue

        word = ''.join(word)


def main():
    char = string.ascii_letters + string.digits + string.punctuation
    guess(char, 8)

if __name__ == '__main__':
    # timer = time()
    main()
    # logging.info(time() - timer)
