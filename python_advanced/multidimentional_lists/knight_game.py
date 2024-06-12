n = int(input())
field = [list(input()) for _ in range(n)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (-1, -2),
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1),
)

removed_knights = 0


while True:
    most_attacks = 0
    knight_position = []

    for row in range(n):
        for col in range(n):
            if field[row][col] == "K":
                attacks_made = 0

                for position in positions:
                    position_row = row + position[0]
                    position_col = col + position[1]

                    if 0 <= position_row < n and 0 <= position_col < n:
                        if field[position_row][position_col] == "K":
                            attacks_made += 1

                if attacks_made > most_attacks:
                    most_attacks = attacks_made
                    knight_position = [row, col]

    if knight_position:
        r, c = knight_position
        field[r][c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)




