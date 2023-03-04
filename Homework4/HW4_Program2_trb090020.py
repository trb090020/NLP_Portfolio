# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 4 - N-Grams: Program 2

import pickle
import pathlib
import math


if __name__ == '__main__':
    # unpickle the dictionaries
    eng_bigram_data = pickle.load(open('eng_bigram_data.p', 'rb'))
    eng_unigram_data = pickle.load(open('eng_unigram_data.p', 'rb'))
    fra_bigram_data = pickle.load(open('fra_bigram_data.p', 'rb'))
    fra_unigram_data = pickle.load(open('fra_unigram_data.p', 'rb'))
    ita_bigram_data = pickle.load(open('ita_bigram_data.p', 'rb'))
    ita_unigram_data = pickle.load(open('ita_unigram_data.p', 'rb'))
    # open and read in the test file LangId.test
    test_path = pathlib.Path.cwd().joinpath('./LangId.test')
    with open(test_path, 'r', encoding='utf-8') as f:
        test_data = f.read()
    # create a file for the probabilities
    # using the 'w' parameter ensures that the file starts empty
    prob_file = open('LangId.calc', 'w', encoding='utf-8')
    prob_file.close()
    # get the lines
    test_lines = test_data.split('\n')
    # for each line, calculate the probability that the line is
    # English, French, or Italian and write the language with the
    # highest probability to a file
    for line in test_lines:
        # split the line into tokens
        tokens = line.split(' ')
        # form unigrams and bigrams of the tokens
        unigrams = tokens
        bigrams = [(unigrams[i], unigrams[i+1]) for i in range(len(unigrams)-1)]
        # calculate probabilities
