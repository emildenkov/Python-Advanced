longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [x.split(",") for x in input().split("-")]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    curr_intersection = first_set.intersection(second_set)

    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = curr_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

