# AUTHOR: Thomas Bennett - trb090020
# COURSE: CS 4395.001 - UTD Spring 2023
# Chatbot Project

import sys
import pathlib


def chat():
    # get user input
    x = input()
    # respond
    print(f'You said: {x}')
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
        # Form a Path object
        datafile = pathlib.Path.cwd().joinpath(sys.argv[1])
        # Check if the file exists
        if confirm_path(datafile):
            print('Welcome to python-chat!')
            print("This chatbot will carry on a dialogue based on quotes from Monty Python's Flying Circus")
            print('Enter "Quit" at any time to quit chatting.')
            print(f'Welcome back, {sys.argv[1]}')
            # load the file for the user
            while True:
                # chat with the user until the user enters "Quit"
                chat_instance = chat()
                if not chat_instance.lower() in ['quit']:
                    continue
                # fall-through break to prevent infinite loop
                break

        else:
            print(f'User name: {sys.argv[1]} was not found, creating a new user profile...')
            # create a file for the user
            print('Welcome to python-chat!')
            print("This chatbot will carry on a dialogue based on quotes from Monty Python's Flying Circus")
            print('Enter "Quit" at any time to quit chatting.')
            while True:
                # chat until the user enters 'quit'
                chat_instance = chat()
                if not chat_instance.lower() in ['quit']:
                    continue
                # fall-through break to prevent infinite loop
                break
