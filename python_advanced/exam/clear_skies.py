def print_field():
    for row in field:
        print(''.join(row))


n = int(input())

field = []
plane_pos = []
armor_value = 300
enemy_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    data = list(input())

    if "J" in data:
        col = data.index("J")
        plane_pos = [row, col]

    enemy_count += data.count("E")
    field.append(data)

field[plane_pos[0]][plane_pos[1]] = "-"

while True:

    if enemy_count == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break

    if armor_value == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{plane_pos[0]}, {plane_pos[1]}]!")
        break

    direction = input()

    row, col = plane_pos
    row_move, col_move = directions[direction]
    r = row + row_move
    c = col + col_move

    element = field[r][c]
    plane_pos = [r, c]

    if element == "-":
        continue

    if element == "R":
        armor_value = 300
        field[r][c] = "-"

    elif element == "E":
        enemy_count -= 1
        if enemy_count == 0:
            continue
        armor_value -= 100
        if armor_value == 0:
            continue
        field[r][c] = '-'


field[plane_pos[0]][plane_pos[1]] = "J"
print_field()
