# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 2 - Word Guess Game

import sys
import pathlib

def calcdiv(pathobj):
    """Calculates and prints the lexical diversity of the text"""

def preprocess(pathobj):
    """
    Preprocesses the raw text:
    1. convert all words to lower-case
    2. remove tokens that are not alphabetical, remove NLTK stopwords,
       and any words with less than 6 letters
    3. lemmatize the tokens
    4. print the first 20 tagged parts-of-speech (POS)
    5. create list of only those lemmas that are nouns
    6. print the number of tokens from step 1 and the number of nouns from step 5
    7. return tokens from step 1 and nouns from step 5
    :param pathobj:
    :return: tokens, nouns
    """
    tokens = []
    nouns = []

    return tokens, nouns


def makegamedict(tokenlist, nounlist):
    """Returns a dictionary of {noun:count of noun in tokenlist}"""
    gamedict = {}

    return gamedict


def guessgame(gamedict):
    """Plays Word Guess Game with the user"""
    print("Welcome to Word Guess Game!")


def confirm_path(filepath):
    """Returns true if a file exists with the given file path name"""
    return pathlib.Path(filepath).is_file()


if __name__ == '__main__':
    # One argument expected, otherwise the program halts
    if not len(sys.argv) == 2:
        print('Provide the path to the data file as an argument')
    else:
        # Form a Path object
        datafile = pathlib.Path.cwd().joinpath(sys.argv[1])
        # Check if the file exists
        if confirm_path(datafile):
            # process the text
            calcdiv(datafile)
            tokens, nouns = preprocess(datafile)
            gamedict = makegamedict(tokens, nouns)
            guessgame(gamedict)

        else:
            print('The file provided does not exist')
