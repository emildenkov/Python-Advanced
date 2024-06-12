from collections import deque

programmers = deque([int(x) for x in input().split()])
number_tasks = deque([int(x) for x in input().split()])

ducks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while programmers and number_tasks:
    prog = programmers.popleft()
    task = number_tasks.pop()
    result = prog * task

    if 0 < result <= 60:
        ducks["Darth Vader Ducky"] += 1

    elif 60 < result <= 120:
        ducks["Thor Ducky"] += 1

    elif 120 < result <= 180:
        ducks["Big Blue Rubber Ducky"] += 1

    elif 180 < result <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1

    else:
        programmers.append(prog)
        number_tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, value in ducks.items():
    print(f"{duck}: {value}")


