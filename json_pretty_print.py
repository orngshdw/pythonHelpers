"""
Code example that copies json from stdin and pretty prints json to terminal. Same as doing "cat <json file> | python -m json.tool"
Usage: cat <json file> | python json_pretty_print.py
"""
import argparse
import json
import sys


def help_text():
    """
    Shows help text (top of file) when user does: python json_pretty_print.py -h
    """
    text = argparse.ArgumentParser(
        description='Code example that prints json content to terminal in pretty format. Same as doing "cat <json file> | python -m json.tool"',
        usage='cat <json file> | python %(prog)s').parse_args()
    return text


def main():
    """
    Reads the a json file outputted to stdin, converts it to a dictionary, and then
    prints to CLI in pretty json format.

    :return: None
    """
    help_text()

    # grabbing lines from stdin
    file_content = ""
    for line in sys.stdin:
        file_content += line

    # converts the json into a dictionary
    all_reactions = json.loads(file_content)
    
    # prints to terminal
    print(json.dumps(all_reactions, sort_keys=True, indent=4))
    

if __name__ == "__main__":
    main()

