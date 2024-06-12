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