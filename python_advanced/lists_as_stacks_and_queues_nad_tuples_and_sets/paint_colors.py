from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}

colors_made = {
    "orange": {"red", "yellow"},
    "green": {"yellow", "blue"},
    "purple": {"red", "blue"}
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break

    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                words.insert(len(words) // 2, el)


for color in set(colors_made.keys()).intersection(result):
    if not colors_made[color].issubset(result):
        result.remove(color)

print(result)





