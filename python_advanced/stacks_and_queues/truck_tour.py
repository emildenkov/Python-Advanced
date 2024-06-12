from collections import deque

pump_data = deque([[int(x) for x in input().split()]for _ in range(int(input()))])

pumps_data_copy = pump_data.copy()
fuel = 0
index = 0

while pumps_data_copy:

    petrol, distance = pumps_data_copy.popleft()

    fuel += petrol

    if fuel >= distance:
        fuel -= distance

    else:
        pump_data.rotate(-1)
        pumps_data_copy = pump_data.copy()
        index += 1
        fuel = 0


print(index)
