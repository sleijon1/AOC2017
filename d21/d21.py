from copy import deepcopy
from math import sqrt

# ---------------------- Creating patterns  ---------------------- #
LINES = open("test.txt").readlines()
def reflect_x(square: list) -> [str]:
    list.reverse(square)
    return square

def reflect_y(square: list) -> [str]:
    for i, row in enumerate(square):
        square[i] = row[::-1]
    return square

patterns = {}

for line in LINES:
    pattern, enhancement = line.split('=>')
    rows = pattern.strip(' ').split('/')
    permutations = []
    permutations.append(''.join(list(rows)))
    permutations.append(''.join(reflect_x(list(rows))))
    permutations.append(''.join(reflect_y(list(rows))))
    permutations.append(''.join(reflect_x(reflect_y(list(rows)))))
    for perm in permutations:
        patterns[perm] = ''.join(enhancement.strip().split('/'))
#print(patterns)
# ---------------------- Creating patterns  ---------------------- #

START_PATTERN = "#..#........#..#"

def split_square(square):
    size = int(sqrt(len(square)))
    if size % 2 == 0:
        squares_per_row = size // 2
        new_squares = []
        for col in range(0, size, 2):
            for row in range(0, size, 2): # 2x2 squares
                new_square = ""
                row = row+(col*size)
                new_square = square[row:row+2]
                new_square += square[row+size:row+size+2]
                #print(new_square)
                new_squares.append(patterns[new_square])
        new_square = ""
        new_size = (len(new_squares)//2)*3
        separated = []
        for square in new_squares:
            #print([square[i:i+3] for i in range(0, len(square), 3)])
            separated.append([square[i:i+3] for i in range(0, len(square), 3)])
        print(separated)
        rows = []
        layer_squares = len(new_squares)//2
        for i in range(0, len(new_squares), layer_squares):
            print(separated[i:i+1])
    elif size % 3 == 0:
        pass

    pass

split_square(START_PATTERN)
