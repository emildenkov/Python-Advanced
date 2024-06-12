def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
field = []

targets = 0
targets_down = 0
targets_position = []

my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]

    targets += field[row].count("x")

for _ in range(int(input())):
    command_data = input().split()

    if command_data[0] == "move":
        my_position = move(command_data[1], int(command_data[2]))

    elif command_data[1] == "shoot":
        target_down_position = shoot(command_data[1])

        if target_down_position:
            targets_down += 1
            targets_position.append(target_down_position)

        if targets_down == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_down < targets:
    print(f"Training not completed! {targets - targets_down} targets left.")

print(*targets_position, sep="\n")
