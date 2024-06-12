# even_lines

symbols = ("-", ",", ".", "!", "?")

with open("resources/text_1.txt", "r") as file:
    text = file.readlines()


for line in range(0, len(text), 2):

    for symbol in symbols:
        text[line] = text[line].replace(symbol, "@")

    print(*text[line].split()[::-1])


# line_numbers

from string import punctuation

with open("resources/text_1.txt", "r") as file:
    text = file.readlines()

output_file = open("resources/output_file.txt", "w")

for line in range(len(text)):
    letters = 0
    symbols = 0

    for symbol in text[line]:
        if symbol.isalpha():
            letters += 1

        if symbol in punctuation:
            symbols += 1

    output_file.write(f"Line {line + 1}: {text[line][:-1]} ({letters})({symbols})\n")

output_file.close()

# file_manipulator

import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        with open(f"resources/{info[0]}", "w"): pass

    elif command == "Add":
        with open(f"resources/{info[0]}", "a") as file:
            file.write(f"{info[0]}\n")

    elif command == "Replace":
        try:
            with open(f"resources/{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("The file does not exist!")

    elif command == "Delete":
        try:
            os.remove(f"resources/{info[0]}")

        except FileNotFoundError:
            print(f"The file {info[0]} was not found and can not be deleted!")

    elif command == "End":
        break


# directory_traversal

import os


def extensions_filter(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]
        elif os.path.isdir and not first_level:
            extensions_filter(file, first_level=True)


directory = input("Directory: ")
extensions = {}
result = []

try:
    extensions_filter(directory)
except FileNotFoundError:
    print("There is no such directory")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("resources/final_file.txt", "w") as final_file:
    final_file.write("\n".join(result))
