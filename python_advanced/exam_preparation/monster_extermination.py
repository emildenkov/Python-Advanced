from collections import deque

armor_monsters = deque([int(x) for x in input().split(",")])
soldier_attack = [int(x) for x in input().split(",")]

kills = 0

while armor_monsters and soldier_attack:

    armor = armor_monsters.popleft()
    attack = soldier_attack.pop()

    if attack >= armor:
        attack -= armor
        kills += 1
        if soldier_attack:
            soldier_attack[-1] += attack
        elif not soldier_attack and attack > 0:
            soldier_attack.append(attack)

    else:
        armor -= attack
        armor_monsters.append(armor)

if not armor_monsters:
    print("All monsters have been killed!")

if not soldier_attack:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {kills}")



