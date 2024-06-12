n = int(input())
field = []

bunny_position = []
best_direction = None
best_path = []
most_eggs = float('-inf')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    field.append(input().split())

    if "B" in field[row]:
        bunny_position = [row, field[row].index("B")]


for direction, position in directions.items():
    row = bunny_position[0] + position[0]
    col = bunny_position[1] + position[1]

    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if field[row][col] == "X":
            break

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= most_eggs:
        most_eggs = collected_eggs
        best_direction = direction
        best_path = path


print(best_direction)
print(*best_path, sep="\n")
print(most_eggs)




