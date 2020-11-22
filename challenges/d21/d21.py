from copy import deepcopy
from math import sqrt

# ---------------------- Creating patterns  ---------------------- #
LINES = open("input.txt").readlines()
def reflect_x(square: list) -> [str]:
    list.reverse(square)
    return square

def reflect_y(square: list) -> [str]:
    for i, row in enumerate(square):
        square[i] = row[::-1]
    return square

def rotate_90(square: list):
    rows = ['' for _ in range(len(square[0]))]
    for i, row in enumerate(square[::-1]):
        for j, el in enumerate(row):
            rows[j] += el
    return rows
patterns = {}

for line in LINES:
    pattern, enhancement = line.split('=>')
    rows = pattern.strip(' ').split('/')
    permutations = []
    # Cube has 4x3 = 8 Unique rotations and reflections
    permutations.append(''.join(list(rows)))
    permutations.append(''.join(rotate_90(list(rows))))
    permutations.append(''.join(rotate_90(rotate_90(list(rows)))))
    permutations.append(''.join(rotate_90(rotate_90(rotate_90(list(rows))))))
    permutations.append(''.join(reflect_x(rotate_90(list(rows)))))
    permutations.append(''.join(reflect_y(rotate_90(list(rows)))))
    permutations.append(''.join(reflect_x(list(rows))))
    permutations.append(''.join(reflect_y(list(rows))))
    for perm in permutations:
        patterns[perm] = ''.join(enhancement.strip().split('/'))
# ---------------------- Creating patterns  ---------------------- #

START_PATTERN = ".#...####"


def split_square(square: str) -> str:
    """ Split square into 2x2's or 3x3's and enhances
    them into 3x3's or 4x4's according to patterns dict

    Positional arguments:
    square -- square represented as a string
    """
    size = int(sqrt(len(square)))
    printrow = ""
    for i in range(1, len(square)+1):
        printrow += square[i-1]
        if (i) % size == 0:
            printrow = ""
    new_squares = []
    if size % 2 == 0:
        new_square_size = 3
        increment = 2
        layer_squares = size//2
    elif size % 3 == 0:
        new_square_size = 4
        increment = 3
        layer_squares = size//3
    for col in range(0, size, increment):
        for row in range(0, size, increment):
            new_square = ""
            row = row+(col*size)
            new_square = square[row:row+increment]
            new_square += square[row+size:row+size+increment]
            if size % 3 == 0 and size % 2 != 0:
                new_square += square[row+2*size:row+2*size+increment]
            new_squares.append(patterns[new_square])
    rows = []
    for i in range(0, len(new_squares), layer_squares):
        for j in range(0, len(new_squares[0]), new_square_size):
            row = ""
            for k in range(i, i+layer_squares):
                row += new_squares[k][j:j+new_square_size]
            rows.append(row)
    new_square = ''.join(rows)
    return new_square

square = START_PATTERN
for i in range(iterations := 23):
    square = split_square(square)
    if i == 4:
        print("Solution part 1: " + str(list.count(list(square), '#')))
        square = START_PATTERN
    if i == 22:
        print("Solution part 2: " + str(list.count(list(square), '#')))
