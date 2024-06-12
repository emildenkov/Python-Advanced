def cookbook(*recipes):
    cuisine_dict = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisine_dict.keys(), key=lambda x: (-len(cuisine_dict[x]), x))

    result = ""

    for cuisine in sorted_cuisines:
        result += f"{cuisine} cuisine contains {len(cuisine_dict[cuisine])} recipes:\n"

        sorted_recipes = sorted(cuisine_dict[cuisine], key=lambda x: x[0])

        for recipe_name, ingredients in sorted_recipes:
            result += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
