# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 4 - N-Grams: Program1

import sys
import pathlib
from nltk.tokenize import word_tokenize


def confirm_path(filepath):
    """Returns true if a file exists with the given file path name"""
    return pathlib.Path(filepath).is_file()


def preprocess(filepath):
    """Reads in the text, removes the newlines, and tokenizes the text and returns the result"""
    with open(filepath, 'r') as f:
        text = f.read()
    text = text.replace('\n', ' ')
    tokens = word_tokenize(text)
    return tokens


def make_grams(tokens):
    """
        Returns a pair of dictionaries
        {bigram -> count pairs}
        {unigram -> count pairs}
    """
    unigrams = tokens
    bigrams = [(unigrams[i], unigrams[i+1]) for i in range(len(unigrams))]
    bigram_counts = {b: bigrams.count(b) for b in set(bigrams)}
    unigram_counts = {u: unigrams.count(u) for u in set(unigrams)}

    return bigram_counts, unigram_counts


if __name__ == '__main__':
    # One argument expected, otherwise the program halts
    if not len(sys.argv) == 2:
        print('Provide the path to the data file as an argument')
    else:
        # Form a Path object
        datafile = pathlib.Path.cwd().joinpath(sys.argv[1])
        # Check if the file exists
        if confirm_path(datafile):
            # preprocess - remove newlines and tokenize
            token_data = preprocess(datafile)
            # create the bigram and unigram dictionaries
            bigram_data, unigram_data = make_grams(token_data)

        else:
            print('The file provided does not exist')
