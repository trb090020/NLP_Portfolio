# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 2 - Word Guess Game

import sys
import pathlib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def calcdiv(pathobj):
    """Calculates and prints the lexical diversity of the text"""
    with open(pathobj, 'r') as f:
        text = f.read()

    text = text.replace('\n', ' ')
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens if t.isalpha() and t not in stopwords.words('english')]
    token_set = set(tokens)
    print("Lexical diversity: %.2f" % (len(token_set) / len(tokens)))
    return tokens


def preprocess(tokens):
    """
    Preprocesses the raw text:
    1. lemmatize the tokens
    2. print the first 20 tagged parts-of-speech (POS)
    3. create list of only those lemmas that are nouns
    4. print the number of tokens and the number of nouns
    5. return nouns from step 4
    :param tokens:
    :return: nouns
    """
    nouns = []

    return nouns


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
            tokens = calcdiv(datafile)
            # nouns = preprocess(tokens)
            # gamedict = makegamedict(tokens, nouns)
            # guessgame(gamedict)

        else:
            print('The file provided does not exist')
