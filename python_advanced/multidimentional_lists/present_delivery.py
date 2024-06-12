def cookies(amount_presents, good_kids_visited):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == "V":
                good_kids_visited += 1

            neighbourhood[r][c] = "-"
            amount_presents -= 1

        if not amount_presents:
            break

    return amount_presents, good_kids_visited


presents = int(input())
size = int(input())

neighbourhood = []
santa_pos = []

nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    neighbourhood.append(input().split())

    if "S" in neighbourhood[row]:
        santa_pos = [row, neighbourhood[row].index("S")]
        neighbourhood[row][santa_pos[1]] = "-"

    nice_kids += neighbourhood[row].count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    current_house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if current_house == "V":
        nice_kids_visited += 1
        presents -= 1

    elif current_house == "C":
        presents, nice_kids_visited = cookies(presents, nice_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == nice_kids:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids > nice_kids_visited:
    print(f"Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")
