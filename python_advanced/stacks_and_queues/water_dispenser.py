from collections import deque

quantity = int(input())

name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        requested_water = int(data[0])
        person = people.popleft()

        if quantity >= requested_water:
            print(f"{person} got water")
            quantity -= requested_water

        else:
            print(f"{person} must wait")

    else:
        _ = data[0]
        litters_refill = int(data[1])
        quantity += litters_refill

    command = input()

print(f'{quantity} liters left')

