def valid_index(curr_indexes):
    return {curr_indexes[0], curr_indexes[2]}.issubset(valid_row) and {curr_indexes[1],
                                                                       curr_indexes[3]}.issubset(valid_col)


def swap_indexes(command, indexes):
    if len(indexes) == 4 and valid_index(indexes) and command == "swap":
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_row = range(rows)
valid_col = range(cols)

while True:
    command_data, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if command_data == "END":
        break

    swap_indexes(command_data, data)
