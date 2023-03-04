# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 4 - N-Grams: Program 1

import pathlib
from nltk.tokenize import word_tokenize
import pickle


def confirm_path(filepath):
    """Returns true if a file exists with the given file path name"""
    return pathlib.Path(filepath).is_file()


def preprocess(filepath):
    """Reads in the text, removes the newlines, and tokenizes the text and returns the result"""
    with open(filepath, 'r', encoding='utf-8') as f:
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
    bigrams = [(unigrams[i], unigrams[i+1]) for i in range(len(unigrams)-1)]
    bigram_counts = {b: bigrams.count(b) for b in set(bigrams)}
    unigram_counts = {u: unigrams.count(u) for u in set(unigrams)}

    return bigram_counts, unigram_counts


if __name__ == '__main__':
    # Form Path objects
    datafile_eng = pathlib.Path.cwd().joinpath('./LangId.train.English')
    datafile_fra = pathlib.Path.cwd().joinpath('./LangId.train.French')
    datafile_ita = pathlib.Path.cwd().joinpath('./LangId.train.Italian')
    # Check if the files exist
    if confirm_path(datafile_eng) and confirm_path(datafile_fra) and confirm_path(datafile_ita):
        # preprocess - remove newlines and tokenize
        eng_token_data = preprocess(datafile_eng)
        fra_token_data = preprocess(datafile_fra)
        ita_token_data = preprocess(datafile_ita)
        # create the bigram and unigram dictionaries
        eng_bigram_data, eng_unigram_data = make_grams(eng_token_data)
        fra_bigram_data, fra_unigram_data = make_grams(fra_token_data)
        ita_bigram_data, ita_unigram_data = make_grams(ita_token_data)
        # pickle the dictionaries
        pickle.dump(eng_bigram_data, open('eng_bigram_data.p', 'wb'))
        pickle.dump(eng_unigram_data, open('eng_unigram_data.p', 'wb'))
        pickle.dump(fra_bigram_data, open('fra_bigram_data.p', 'wb'))
        pickle.dump(fra_unigram_data, open('fra_unigram_data.p', 'wb'))
        pickle.dump(ita_bigram_data, open('ita_bigram_data.p', 'wb'))
        pickle.dump(ita_unigram_data, open('ita_unigram_data.p', 'wb'))

    else:
        print('File read issue(s).\nProgram 1 expects 3 data files in the working directory')
        print('Expected file names:\n', 'LangId.train.English', 'LangId.train.French',
              'LangId.train.Italian', sep='')
