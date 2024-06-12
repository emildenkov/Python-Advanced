def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())

    for index in range(len(numbers)):
        key = keys[index % 4]

        if key == "a":
            kwargs[key] += numbers[index]

        elif key == "s":
            kwargs[key] -= numbers[index]

        elif key == "d":
            if numbers[index] != 0:
                kwargs[key] /= numbers[index]

        elif key == "m":
            kwargs[key] *= numbers[index]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)
 

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))