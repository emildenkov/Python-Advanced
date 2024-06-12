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
