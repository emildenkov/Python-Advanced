def check_valid(curr_row, curr_col):
    return 0 <= curr_row < n and 0 <= curr_col < n


def move(curr_direction):
    current_row, current_col = squirrel_pos
    row_move, col_move = directions[curr_direction]
    r = current_row + row_move
    c = current_col + col_move
    return r, c


n = int(input())
direction = input().split(", ")

matrix = []
hazelnuts = 0
squirrel_pos = []
die = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    info = list(input())

    if "s" in info:
        col = info.index("s")
        squirrel_pos = [row, col]

    matrix.append(info)

matrix[squirrel_pos[0]][squirrel_pos[1]] = "*"

for dir in direction:
    row, col = move(dir)

    if not check_valid(row, col):
        print("The squirrel is out of the field.")
        die = True
        break

    squirrel_pos = [row, col]

    if matrix[row][col] == "*":
        continue
    elif matrix[row][col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        die = True
        break
    elif matrix[row][col] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()


if die == False and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")