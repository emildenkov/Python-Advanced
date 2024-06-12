from collections import deque

fuel = deque([int(x) for x in input().split()])
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

altitude_names = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])

altitudes_with_values = {}
for i in altitude_names:
    if needed_fuel:
        value = needed_fuel.popleft()
        altitudes_with_values[i] = value

reached_altitudes = []

while fuel and consumption and altitudes_with_values:
    level = altitude_names[0]
    current_fuel = fuel[-1]
    current_consumption = consumption[0]

    balance = current_fuel - current_consumption

    if balance < altitudes_with_values[level]:
        fuel.pop()
        consumption.popleft()
        altitude_names.popleft()
        print(f"John did not reach: {level}")
        break
    else:
        fuel.pop()
        consumption.popleft()
        reached_altitudes.append(level)
        del altitudes_with_values[level]
        altitude_names.popleft()
        print(f"John has reached: {level}")

if not altitudes_with_values:
    print(f"John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if reached_altitudes:
        print(f"Reached altitudes:", ", ".join(reached_altitudes))
    else:
        print("John didn't reach any altitude.")



