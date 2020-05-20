"""Map letters from string into dictionary and print pbar chart of frequency."""
import sys
import pprint
from collections import defaultdict



ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def bag_of_letters():
    phrase = input("Type a short phrase (like a tweet!):")

    mapped = defaultdict(list)
    print(mapped)

    for character in phrase:
        character = character.lower()
        if character in ALPHABET:
            mapped[character].append(character)
            #print(mapped)

    print("\nYou may need to stretch console window if text wrapping occurs.\n")
    print("text = ", end='')
    print(f"{phrase}")
    pprint.pprint(mapped, width=110)

if __name__ == "__main__":
    bag_of_letters()

