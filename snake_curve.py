import numpy as np
import cv2
import sys

def snake(rows, cols):
    transformed = []
    row_even = np.arange(cols)
    for row in np.arange(rows):
        if row%2 == 0:
            cols_list = row_even
        else:
            cols_list = row_even[::-1]
        for col in cols_list:
            transformed.append((row, col))

    return transformed 


def snake_gen(rows, cols):
    row_even = np.arange(cols)
    for row in np.arange(rows):
        if row%2 == 0:
            cols_list = row_even
        else:
            cols_list = row_even[::-1]
        for col in cols_list:
            yield (row, col)


if __name__ == '__main__':
    sn = snake_gen(1e3, 1e3)
    for x in sn:
        print(x)

    reg_map = snake(1e3, 1e3)
    print('size new_map:', sys.getsizeof(sn))
    print('size reg_map:', sys.getsizeof(reg_map))

