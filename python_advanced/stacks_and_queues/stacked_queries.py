numbers = []

for _ in range(int(input())):
    data = input().split()
    command = data[0]

    if command == '1':
        num = data[1]
        numbers.append(num)

    elif command == '2':
        if numbers:
            numbers.pop()

    elif command == '3':
        if numbers:
            print(max(numbers))

    elif command == '4':
        if numbers:
            print(min(numbers))

numbers.reverse()

print(*numbers, sep=", ")
