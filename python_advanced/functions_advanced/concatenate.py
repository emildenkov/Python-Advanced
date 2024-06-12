def concatenate(*part_words, **replace):
    text = "".join(part_words)

    for key, value in replace.items():
        text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))