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

