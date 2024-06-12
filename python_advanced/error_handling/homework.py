# numbers_dictionary

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except ValueError:
        print("")
    line = input("Number does not exist in dictionary")

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)

# email_validator

import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainDigits(Exception):
    pass


class NoWhiteSpace(Exception):
    pass


pattern = r"/\S+/"
MIN_SYMBOLS = 4
EXTENSION = ("com", "bg", "org", "net")

email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) <= MIN_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split(".")[-1] not in EXTENSION:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    digits_counter = 0
    for symbol in email:
        if symbol.isdigit():
            digits_counter += 1

    if digits_counter <= 2:
        raise MustContainDigits("Email must contain at least two digits!")

    if not re.fullmatch(pattern, email):
        raise NoWhiteSpace("Email should not contain any whitespaces!")

    print("Email is valid")
    email = input()