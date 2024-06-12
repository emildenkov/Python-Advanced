n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[row][row] for row in range(n)]
secondary_diagonal = [matrix[row][n - row - 1] for row in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

