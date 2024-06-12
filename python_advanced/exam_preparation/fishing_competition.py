def check_valid_pos(direction):
    r, c = ship_pos
    next_r = r + directions[direction][0]
    next_c = c + directions[direction][1]

    next_r = (next_r + len(fishing_area)) % len(fishing_area)
    next_c = (next_c + len(fishing_area)) % len(fishing_area)

    return next_r, next_c


n = int(input())
fishing_area = []

ship_pos = []
tons_fish = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    data = list(input())

    if "S" in data:
        ship_pos = [row, data.index("S")]

    fishing_area.append(data)
    fishing_area[ship_pos[0]][ship_pos[1]] = "-"

command = input()

while command != "collect the nets":

    row, col = check_valid_pos(command)

    ship_pos = [row, col]
    symbol = fishing_area[row][col]
    fishing_area[row][col] = "-"

    if symbol == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship"
              f": [{ship_pos[0]},{ship_pos[1]}]")
        exit()
    elif symbol.isdigit():
        tons_fish += int(symbol)

    command = input()

fishing_area[ship_pos[0]][ship_pos[1]] = "S"

if tons_fish <= 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - tons_fish} tons of fish more.")
else:
    print("Success! You managed to reach the quota!")

if tons_fish > 0:
    print(f"Amount of fish caught: {tons_fish} tons.")

for row in fishing_area:
    print(f"{''.join(row)}")
