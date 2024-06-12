odd = set()
even = set()

for row in range(1, int(input()) + 1):
    sum_name = sum(ord(x) for x in input()) // row

    if sum_name // 2 == 0:
        even.add(sum_name)
    else:
        odd.add(sum_name)

sum_odd, sum_even = sum(odd), sum(even)

if sum_odd == sum_even:
    print(*odd.union(even), sep=", ")
elif sum_odd > sum_even:
    print(*odd.difference(even), sep=", ")
elif sum_odd < sum_even:
    print(*odd.symmetric_difference(even), sep=", ")
