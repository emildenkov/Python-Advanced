def age_assignment(*names, **kwargs):

    print_age = []

    for letter, age in kwargs.items():
        for name in names:
            if name.startswith(letter):
                print_age.append(f"{name} is {age} years old.")

    return "\n".join(sorted(print_age))


print(age_assignment("Peter", "George", G=26, P=19))