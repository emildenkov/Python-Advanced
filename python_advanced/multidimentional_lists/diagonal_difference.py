n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

primary_diagonal = [matrix[row][row] for row in range(n)]
secondary_diagonal = [matrix[row][n - row - 1] for row in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
