from collections import deque

num = deque(input().split())

while num:
    popped_num = num.pop()
    print(popped_num, end=" ")

