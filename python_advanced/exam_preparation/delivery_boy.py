def check_valid(curr_row, curr_col):
    return 0 <= curr_row < n and 0 <= curr_col < m


def print_neighborhood():
    for row in neighbourhood:
        print(''.join(row))


n, m = [int(x) for x in input().split()]

neighbourhood = []
starting_pos = None

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    info = list(input())

    if "B" in info:
        col = info.index("B")
        starting_pos = (row, col)

    neighbourhood.append(info)

current_pos = starting_pos

while True:
    direction = input()

    row, col = current_pos
    row_move, col_move = directions[direction]
    r = row + row_move
    c = col + col_move

    if not check_valid(r, c):
        neighbourhood[starting_pos[0]][starting_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    element = neighbourhood[r][c]

    if element == "*":
        continue

    current_pos = [r, c]

    if element == "P":
        neighbourhood[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif element == "A":
        neighbourhood[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif element == "-":
        neighbourhood[r][c] = "."


print_neighborhood()