n = int(input())
matrix = []
alice_position = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[row][alice_position[1]] = "*"


while tea_bags < 10:
    direction = input()

    row = directions[direction][0] + alice_position[0]
    col = directions[direction][1] + alice_position[1]

    if not (0 <= row < n and 0 <= col < n):
        break

    alice_position = [row, col]
    element = matrix[row][col]
    matrix[row][col] = '*'

    if element == "R":
        break

    if element.isdigit():
        tea_bags += int(element)


if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]



