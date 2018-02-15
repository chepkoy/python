# while True:
#     respose = input()
#     if int(respose) % 7 == 0:
#         break

# For Loops
# towns = ["Nairobi", "Kisumu", "Eldoret", "Mombasa"]
# for town in towns:
#     print(town)

#!/usr/bin/env python3 
""" Retrieve and prints words from a URL.

Usage:
    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen 
def fetch_words(url):
    """Fetch a list of words from URL

    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split() 
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(items):
    """Prints items one per line.

    Args:
        An iterable series of printable items.
    """
    for items in items:
        print(items)


def main(url):
    """Prints each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)


if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename
