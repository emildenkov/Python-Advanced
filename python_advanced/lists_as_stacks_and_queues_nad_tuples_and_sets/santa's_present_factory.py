from collections import deque

materials = deque([int(el) for el in input().split()])
magic_level = deque([int(el) for el in input().split()])
crafted = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}


while materials and magic_level:
    material = materials.pop() if magic_level[0] or not materials[-1] else 0
    magic = magic_level.popleft() if material or not magic_level[0] else 0

    if not magic:
        continue

    product = material * magic

    if presents.get(product):
        crafted.append(presents[product])

    elif product < 0:
        materials.append(material + magic)

    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
