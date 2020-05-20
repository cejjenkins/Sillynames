"""Translate text into pig latin."""
import sys

consonant = 'bcdfghjklmnpqrstvwxyz'

vowel = 'aeiou'

def pig_latin():
    while True:
        word = input("Type a word and get it's Pig Latin translation:")

        if word[0] in consonant:
            pig_latin = word[1:] + word[0] + 'ay'
        elif word[0] in vowel:
                pig_latin = word + 'way'
        else:
            TypeError("Are you sure this is a word?")
        print(f'{pig_latin}')

        try_again = input("\n\nTry again? (Press Enter else n to stop)\n")
        if try_again.lower()=="n":
            sys.exit()


if __name__ == "__main__":
    pig_latin()

