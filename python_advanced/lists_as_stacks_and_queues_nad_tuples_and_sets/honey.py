from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())

total_honey_made = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b
}


while bees and nectar:

    curr_bee = bees.popleft()
    amount_nectar = nectar.pop()

    if amount_nectar < curr_bee:
        bees.appendleft(curr_bee)
        continue

    else:
        total_honey_made += abs(functions[symbols.popleft()](curr_bee, amount_nectar))

print(f"Total honey made: {total_honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(nec) for nec in nectar)}")

