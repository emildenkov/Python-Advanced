from collections import deque


def fill_the_box(height, length, width, *numbers):
    space = height * length * width
    cubes = deque(numbers)

    while cubes:
        if cubes[0] == "Finish":
            break

        space -= cubes.popleft()

        if space < 0:
            cubes_left = sum(cube for cube in cubes if cube != "Finish")
            return f"There is free space in the box. You could put {cubes_left + abs(space)} more cubes."

    return f"No more free space! You have {space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
