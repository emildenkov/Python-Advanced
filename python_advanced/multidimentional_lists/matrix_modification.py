n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while True:

    if command[0] == "END":
        break

    command_type, r, c, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < n and 0 <= c < n):
        print("Invalid coordinates")
        continue

    elif command_type == "Add":
        matrix[r][c] += value

    elif command_type == "Subtract":
        matrix[r][c] -= value

    command = input().split()


[print(*row) for row in matrix]



