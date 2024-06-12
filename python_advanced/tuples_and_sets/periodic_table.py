periodic_table = set()

for _ in range(int(input())):
    for element in input().split():
        periodic_table.add(element)


print(*periodic_table, sep="\n")

