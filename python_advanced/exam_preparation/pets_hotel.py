def accommodate_new_pets(capacity_hotel, maximum_weight, *pets):
    capacity = capacity_hotel
    weight = maximum_weight
    accommodated_pets = {}
    all_accommodated = True

    for animal, animal_weight in pets:
        if not capacity:
            all_accommodated = False
            break

        if animal_weight <= weight:
            if animal not in accommodated_pets:
                accommodated_pets[animal] = 0
            accommodated_pets[animal] += 1
            capacity -= 1

    result = ''
    if not all_accommodated:
        result += "You did not manage to accommodate all pets!\n"
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"

    if accommodated_pets:
        sorted_pets = sorted(accommodated_pets.items(), key=lambda x: (x[0]))
        for p, n in sorted_pets:
            result += f"{p}: {n}\n"

    return result[:-1]


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


