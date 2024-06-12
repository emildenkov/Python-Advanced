from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = deque([int(x) for x in input().split()])

while tools and substances:

    tool = tools.popleft()
    substance = substances[-1]
    result = tool * substance

    if result in challenges:
        substances.pop()
        challenges.remove(result)
        continue

    tool += 1
    tools.append(tool)
    substances[-1] -= 1
    if substances[-1] <= 0:
        substances.pop()


if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f'Tools: {", ".join([str(x) for x in tools])}')

if substances:
    print(f'Substances: {", ".join([str(x) for x in substances])}')

if challenges:
    print(f'Challenges: {", ".join([str(x) for x in challenges])}')



