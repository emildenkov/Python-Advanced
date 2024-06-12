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




