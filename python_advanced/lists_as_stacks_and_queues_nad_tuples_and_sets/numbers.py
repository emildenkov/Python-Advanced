# first_set = set([x for x in input().split()])
# second_set = set([x for x in input().split()])
#
# functions = {
#     "Add First": lambda x: [first_set.add(el) for el in x],
#     "Add Second": lambda x: [second_set.add(el) for el in x],
#     "Remove First": lambda x: [first_set.discard(el) for el in x],
#     "Remove Second": lambda x: [second_set.discard(el) for el in x],
#     "Check Subset": lambda x: print([first_set.issubset(second_set) or second_set.issubset(first_set)]),
# }
#
#
# for _ in range(int(input())):
#     word_1, word_2, *data = input().split()
#
#     command = word_1 + " " + word_2
#
#     functions[command](data)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")


first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())


for _ in range(int(input())):
    word_1, word_2, *data = input().split()

    command = word_1 + " " + word_2

    if command == "Add First":
        first_set.add(int(el) for el in data)

    elif command == "Add Second":
        second_set.add(int(el) for el in data)

    elif command == "Remove First":
        first_set.discard(int(el) for el in data)

    elif command == "Remove Second":
        second_set.discard(int(el) for el in data)

    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

sorted_first = sorted(first_set)
sorted_second = sorted(second_set)

print(*sorted_first, sep=", ")
print(*sorted_second, sep=", ")




