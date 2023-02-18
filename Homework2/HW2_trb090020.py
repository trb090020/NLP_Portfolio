# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 2 - Word Guess Game

import sys
import pathlib
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def calcdiv(pathobj):
    """Calculates and prints the lexical diversity of the text"""
    with open(pathobj, 'r') as f:
        text = f.read()

    text = text.replace('\n', ' ')
    tokens = word_tokenize(text)
    token_set = set(tokens)
    print("Lexical diversity before removing non-alpha tokens and stopwords: %.2f" % (len(token_set) / len(tokens)))
    tokens = [t.lower() for t in tokens if t.isalpha() and t not in stopwords.words('english')]
    token_set = set(tokens)
    print("Lexical diversity after removing non-alpha tokens and stopwords: %.2f" % (len(token_set) / len(tokens)))
    # only keep words with length > 5
    tokens = [t for t in tokens if len(t) > 5]
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
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    uniq_lemmas = list(set(lemmas))
    pos = pos_tag(uniq_lemmas)
    print("First 20 tagged unique lemmas:")
    for i in range(20):
        print(pos[i])

    for u in uniq_lemmas:
        if u[1] == 'NN' or 'NNP' or 'NNS':
            nouns.append(u)

    print("Number of tokens:", len(tokens), sep=' ')
    print("Number of nouns:", len(nouns), sep=' ')
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
            nouns = preprocess(tokens)
            # gamedict = makegamedict(tokens, nouns)
            # guessgame(gamedict)

        else:
            print('The file provided does not exist')
