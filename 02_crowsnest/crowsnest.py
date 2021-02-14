#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2021-02-09
Purpose: Crows's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crows's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    print(word)

    article = ''
    if word[0].lower() in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
