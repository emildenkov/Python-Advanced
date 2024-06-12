n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split())

directions = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
    (1, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (0, 0)
)

for row, col in coordinates:
    if matrix[row][col] < 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]