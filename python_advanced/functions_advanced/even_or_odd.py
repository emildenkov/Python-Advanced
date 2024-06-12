def even_odd(*commands):
    command = commands[-1]

    if command == "even":
        even_nums = [num for num in commands[:-1] if num % 2 == 0]
        return even_nums

    else:
        odd_nums = [num for num in commands[:-1] if num % 2 != 0]
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))