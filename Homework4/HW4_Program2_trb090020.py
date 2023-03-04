# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 4 - N-Grams: Program 2

import pickle
import pathlib


def calc_prob(bigrams, unigram_dict, bigram_dict, cardinality):
    """
    Calculates the probability that the text is a sentence of the language modeled by
    the unigram and bigram dictionaries.
    """
    probability = 1
    for bigram in bigrams:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        probability = probability * ((n + 1) / (d + cardinality))
    return probability


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
    all_unigrams_count = len(eng_unigram_data) + len(fra_unigram_data) + len(ita_unigram_data)
    line_number = 1
    for line in test_lines:
        # split the line into tokens
        tokens = line.split(' ')

        # count the tokens
        line_length = len(tokens)

        # form unigrams and bigrams of the tokens
        line_unigrams = tokens
        line_bigrams = [(line_unigrams[i], line_unigrams[i+1]) for i in range(len(line_unigrams)-1)]

        # calculate probabilities
        eng_prob = calc_prob(line_bigrams,
                             eng_unigram_data,
                             eng_bigram_data,
                             all_unigrams_count)
        fra_prob = calc_prob(line_bigrams,
                             fra_unigram_data,
                             fra_bigram_data,
                             all_unigrams_count)
        ita_prob = calc_prob(line_bigrams,
                             ita_unigram_data,
                             ita_bigram_data,
                             all_unigrams_count)

        # figure out which language is the most likely
        if eng_prob > fra_prob and eng_prob > ita_prob:
            calc_lang = 'English'
        elif fra_prob > ita_prob:
            calc_lang = 'French'
        else:
            calc_lang = 'Italian'

        # write the most likely language to LangId.calc
        with open('LangId.calc', 'a', encoding='utf-8') as f:
            f.write(str(line_number) + ' ' + calc_lang + '\n')

        # increment line number
        line_number += 1

    # get the calculated classifications and solutions
    with open('LangId.calc', 'r', encoding='utf-8') as f:
        calc_data = f.read()
    with open('LangId.sol', 'r', encoding='utf-8') as f:
        sol_data = f.read()

    # calculate the accuracy
    acc_arr = []
    calc_data = calc_data.split('\n')
    sol_data = sol_data.split('\n')
    for i, solution in enumerate(sol_data):
        if solution == calc_data[i]:
            acc_arr.append(1)
        else:
            acc_arr.append(0)
    acc = sum(acc_arr) / len(acc_arr)
    print(f"Model accuracy: {acc}")
