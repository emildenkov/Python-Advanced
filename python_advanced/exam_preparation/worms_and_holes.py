from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
length_worms = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1

    else:
        worm -= 3
        if worm <= 0:
            continue

        worms.append(worm)

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != length_worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
