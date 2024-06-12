def check_valid(curr_row, curr_col, n):
    return 0 <= curr_row < n and 0 <= curr_col < n


def print_board():
    for row in board:
        print(''.join(row))


n = int(input())

board = []
gambler_pos = []
money = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    info = list(input())

    if "G" in info:
        col = info.index("G")
        gambler_pos = [row, col]

    board.append(info)


direction = input()

while direction != "end":
    row, col = gambler_pos
    row_move, col_move = directions[direction]
    r = row + row_move
    c = col + col_move

    if not check_valid(r, c, n):
        print("Game over! You lost everything!")
        exit()

    element = board[r][c]
    board[r][c] = "G"
    board[row][col] = "-"
    gambler_pos = [r, c]

    if element == "W":
        money += 100

    elif element == "P":
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            exit()

    elif element == "J":
        money += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        print_board()
        exit()

    direction = input()


print(f"End of the game. Total amount: {money}$")
print_board()