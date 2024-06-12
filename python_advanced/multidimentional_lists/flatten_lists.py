sequence = [num.split() for num in input().split("|")]
print(*[' '.join(num) for num in sequence[::-1] if num])



