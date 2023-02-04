# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 1 - Text Processing with Python

import sys
import pathlib
import re
import pickle


class Person:

    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("Employee id: " + self.id)
        print("\t\t" + self.first + " " + self.mi + " " + self.last)
        print("\t\t" + self.phone + '\n')


def standardize_data(filepath):
    """Fixes a csv file automatically and with some user input"""
    lines = list(open(filepath))
    people = {}
    for p in lines[1:]:  # Skips the first line
        indiv = p.split(',')

        # fix last name
        last = indiv[0].capitalize()

        # fix first name
        first = indiv[1].capitalize()

        # fix middle initial
        mi = indiv[2]
        if not mi:
            mi = 'X'

        # fix id (iden)
        iden = indiv[3]
        # Create regex object
        id_regex = re.compile("[A-Z]{2}[0-9]{4}")
        while True:
            # Check for pattern match
            if id_regex.fullmatch(iden):
                break
            # Ask for correctly-formed id
            print("ID invalid: " + iden)
            print("ID is two capital letters followed by 4 digits")
            iden = input("Please enter a valid id: ")

        # fix phone number
        phone = indiv[4]
        phone_regex = re.compile("[0-9]{3}-[0-9]{3}-[0-9]{4}")
        while True:
            # Check for pattern match
            if phone_regex.fullmatch(phone):
                break
            # Ask for correctly-formed phone
            print("Phone " + phone + " is invalid")
            print("Enter phone number in form 123-456-7890")
            phone = input("Enter phone number: ")

        # Print error message if the input file contains duplicate ids
        if iden in people:
            print("Alert! There are duplicate ids in the input file!")
        # Create a Person object
        p = Person(last, first, mi, iden, phone)
        # Add the Person to the people dictionary
        people[p.id] = p
    return people


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
            # Process the data
            data = standardize_data(datafile)
            # Pickle the data
            pickle.dump(data, open('fixed_data.p', 'wb'))
            fixed_data = pickle.load(open('fixed_data.p', 'rb'))
            # Confirm the data was pickled successfully
            print("\n" + "Employee list:" + "\n")
            for f in fixed_data.values():
                f.display()
        else:
            print('The file provided does not exist!')
