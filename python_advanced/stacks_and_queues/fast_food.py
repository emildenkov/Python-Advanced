from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food_quantity >= order:
        orders.popleft()
        food_quantity -= order

    else:
        print("Orders left:", *orders)
        break

else:
    print("Orders complete")



