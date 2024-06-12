from collections import deque

money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])

food_eaten = 0

while money and prices:
    initial_money = money[-1]
    initial_price = prices[0]

    if initial_price == initial_money:
        money.pop()
        prices.popleft()
        food_eaten += 1

    elif initial_price > initial_money:
        money.pop()
        prices.popleft()

    elif initial_money > initial_price:
        food_eaten += 1
        change = initial_money - initial_price
        money.pop()
        if money:
            money[-1] += change
        prices.popleft()

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")

elif 1 < food_eaten < 4:
    print(f"Henry ate: {food_eaten} foods.")

elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")

elif not food_eaten:
    print("Henry remained hungry. He will try next weekend again.")