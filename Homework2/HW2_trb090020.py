# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 2 - Word Guess Game
import random
import sys
import pathlib
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def calcdiv(pathobj):
    """
    Calculates and prints the lexical diversity of the text. Since the text
    is tokenized to perform this analysis, the token
    :param pathobj: a pathlib Path object
    :return: tokens: tokenized text
    """
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
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    uniq_lemmas = list(set(lemmas))
    tag_lemmas = pos_tag(uniq_lemmas)

    print("First 20 tagged unique lemmas:")
    for i in range(20):
        print(tag_lemmas[i])
    nouns = [lemma[0] for lemma in tag_lemmas if lemma[1] == 'NN']

    print("Number of tokens:", len(tokens), sep=' ')
    print("Number of unique lemmas:", len(uniq_lemmas), sep=' ')
    print("Number of unique nouns:", len(nouns), sep=' ')

    return nouns


def makegamedata(tokenlist, nounlist):
    """Returns a dictionary of {noun:count of noun in tokenlist}"""
    gamedict = {n: tokenlist.count(n) for n in nounlist}
    return gamedict


def guessgame(gamedict):
    """Plays Word Guess Game with the user"""
    print("\n****** Welcome to Word Guess Game! ******")
    top_nouns = sorted(gamedict, key=gamedict.get, reverse=True)
    top_nouns = top_nouns[:50]
    # Get a random element from top_nouns.
    # Generate a random number (integer) between 0 and the length of top_nouns - 1.
    rand_num = random.randint(0, len(top_nouns) - 1)
    goal = top_nouns[rand_num]
    guesses = 5

    while True:
        print("Cheat for the demo? (Y/anything else)")
        user_input = str(input())
        if user_input in ['y', 'Y']:
            print(goal)
        guesses = guessloop(goal, guesses)
        if guesses < 1:
            print('**************************************************')
            print("Exiting...")
            print('**************************************************')
            break
        print('**************************************************')
        print("Keep playing? (Y/anything else)")
        print('**************************************************')
        user_input = str(input())
        if user_input in ['y', 'Y']:
            top_nouns.remove(goal)
            if len(top_nouns) < 1:
                print('**************************************************')
                print("You used all the words. Exiting...")
                print('**************************************************')
                break
            rand_num = random.randint(0, len(top_nouns) - 1)
            goal = top_nouns[rand_num]
            continue
        else:
            print('**************************************************')
            print("Exiting...")
            print('**************************************************')
            break


def guessloop(goal, guesses):
    board = ['_' for letter in goal]
    letters = []
    while True:
        # Beginning of round - show board and remaining guesses
        print(guesses, " guesses remaining", sep='')
        print("Guessed letters: ", letters, sep='')
        for letter in board:
            print(letter, end=' ')
        print('\n')
        # If zero guesses remain, print game over - failure message and break
        if guesses < 1:
            print('**************************************************')
            print("You ran out of guesses, game over!")
            print('**************************************************')
            break
        # Prompt for user input
        print("Try to guess a letter in the word (or enter ! to give up):")
        x = str(input())
        # Check for exclamation mark - give up
        if x in ['!']:
            break
        # Check that the input was a single letter
        if not len(x) == 1 and x.isalpha():
            print('**************************************************')
            print("Invalid input! You entered: ", x, sep='')
            print("Please only enter a single letter\n")
            print('**************************************************')
            continue
        x = x.lower()
        if x in letters:
            print('**************************************************')
            print("You already guessed ", x, ". Try a different letter.", sep='')
            print('**************************************************')
            continue
        # Check if the input letter is in the word
        if x not in goal:
            guesses -= 1
            letters.append(x)
            print('**************************************************')
            print("Bad luck! You lose a guess.")
            print('**************************************************')
            continue
        # Reaching this line means the letter was found in goal

        for i, letter in enumerate(goal):
            if letter == x:
                board[i] = x
        letters.append(x)
        print('**************************************************')
        print("Good guess! You gain a guess.")
        print('**************************************************')
        guesses += 1
        # Check if the board is completed
        if '_' not in board:
            print('**************************************************')
            print("Congratulations! You solved the word!")
            print('**************************************************')
            for letter in board:
                print(letter, end=' ')
            print('\n')
            break
        continue
    return guesses

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
            token_data = calcdiv(datafile)
            noun_data = preprocess(token_data)
            game_data = makegamedata(token_data, noun_data)
            guessgame(game_data)

        else:
            print('The file provided does not exist')
