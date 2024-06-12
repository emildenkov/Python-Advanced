def shop_from_grocery_list(budget, grocery_list: list, *products_info):
    bought_products = []

    for product, price in products_info:
        if product not in grocery_list:
            continue
        if float(budget) - price < 0:
            break
        else:
            bought_products.append(product)
            grocery_list.remove(product)
            budget -= price

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
