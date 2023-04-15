# AUTHOR: Thomas Bennett - trb090020
# COURSE: CS 4395.001 - UTD Spring 2023
# Chatbot Project

import sys
import pathlib
import pickle
import pprint
"""
python-chat.py - A Monty Python's Flying Circus Chatbot

Source: https://www.ibras.dk/montypython/justthewords.htm

This program uses a dict of sentences from Monty Python's Flying Circus to tell you what the
next sentence after a line that the user provides is.

Example run:
    user>Next we have number four, 'Crunchy Frog'.
    bot>'An, yes.'
    user>Am I right in thinking there's a real frog in here?
    bot>'Yes.'
    user>What sort of frog?
    bot>'A dead frog.'
    user>Is it cooked?
    bot>'No.'
    user>What, a raw frog?
    bot>('We use only the finest baby frogs, dew-picked and flown from Iraq, cleansed in the finest quality spring water, lightly '
        'killed, and then sealed in a succulent Swiss quintuple smooth treble cream milk chocolate envelope, and lovingly frosted '
        'with glucose.')
"""


def chat(prev_next):

    # get user input
    x = input()
    # check if the user entered 'quit'
    if x.lower() in ['quit']:
        return x
    # respond
    try:
        next_sentence = prev_next[x]['next']
        pprint.pprint(next_sentence, width=125)
    except KeyError:
        print('Sorry, that sentence was not found.')

    # return the user input to be saved in their user file
    return x


def confirm_path(filepath):
    """Returns true if a file exists with the given file path name"""
    return pathlib.Path(filepath).is_file()


if __name__ == '__main__':
    # One argument expected, otherwise the program halts
    if not len(sys.argv) == 2:
        print('Provide your name as an argument')
    else:
        # load the prev_next dict
        prev_next = pickle.load(open('flying_circus_prev_next.pickle', 'rb'))
        # Form a Path object
        datafile = pathlib.Path.cwd().joinpath(sys.argv[1] + ".pickle")
        # Check if the file exists
        if confirm_path(datafile):
            print('Welcome to python-chat!')
            print("This chatbot will carry on a dialogue based on quotes from Monty Python's Flying Circus")
            print('Enter "Quit" at any time to quit chatting.')
            print(f'Welcome back, {sys.argv[1]}')

            # load the file for the user
            user_file = pickle.load(open(sys.argv[1] + ".pickle", 'rb'))
            print(f'Your last used prompt was: {user_file[1]}')
            while True:
                # chat with the user until the user enters "Quit"
                chat_instance = chat(prev_next)
                if not chat_instance.lower() in ['quit']:
                    user_file[1] = chat_instance
                    continue
                with open(sys.argv[1] + '.pickle', 'wb') as f:
                    pickle.dump(user_file, f, pickle.HIGHEST_PROTOCOL)
                # fall-through break to prevent infinite loop
                break

        else:
            print(f'User name: {sys.argv[1]} was not found, creating a new user profile...')
            # create a file for the user
            new_user_file = [sys.argv[1], '']
            with open(sys.argv[1] + '.pickle', 'wb') as f:
                pickle.dump(new_user_file, f, pickle.HIGHEST_PROTOCOL)
            print('Welcome to python-chat!')
            print("This chatbot will carry on a dialogue based on quotes from Monty Python's Flying Circus")
            print('Enter "Quit" at any time to quit chatting.')
            while True:
                # chat until the user enters 'quit'
                chat_instance = chat(prev_next)
                if not chat_instance.lower() in ['quit']:
                    new_user_file[1] = chat_instance
                    continue
                with open(sys.argv[1] + '.pickle', 'wb') as f:
                    pickle.dump(new_user_file, f, pickle.HIGHEST_PROTOCOL)
                # fall-through break to prevent infinite loop
                break
