def func_executor(*func_args):
    return "\n".join(f"{func.__name__} - {func(*args)}" for func, args in func_args)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)),(multiply_numbers, (2, 4))))