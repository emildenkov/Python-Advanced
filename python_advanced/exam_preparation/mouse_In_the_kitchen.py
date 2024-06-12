def check_valid(curr_row, curr_col):
    return 0 <= curr_row < n and 0 <= curr_col < m


n, m = [int(x) for x in input().split(",")]

kitchen = []
mouse_pos = []
cheese_count = 0
eaten_cheese = 0
last_direction = ''

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    info = list(input())

    if "M" in info:
        col = info.index("M")
        mouse_pos = [row, col]

    cheese_count += info.count("C")
    kitchen.append(info)

kitchen[mouse_pos[0]][mouse_pos[1]] = "*"

while True:
    direction = input()
    all_cheese = False

    if direction == "danger":
        last_direction = direction
        break

    row, col = mouse_pos
    row_move, col_move = directions[direction]
    r = row + row_move
    c = col + col_move

    if not check_valid(r, c):
        kitchen[row][col] = "M"
        print("No more cheese for tonight!")
        break

    element = kitchen[r][c]

    if element == "@":
        continue

    mouse_pos = [r, c]

    if element == "T":
        kitchen[r][c] = "M"
        print("Mouse is trapped!")
        break

    elif element == "C":
        eaten_cheese += 1
        kitchen[r][c] = "*"
        if eaten_cheese == cheese_count:
            kitchen[r][c] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            all_cheese = True
            break
    if all_cheese:
        break


if last_direction == "danger":
    print("Mouse will come back later!")

for row in kitchen:
    print(''.join(row))
