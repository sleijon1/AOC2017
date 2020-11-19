from copy import deepcopy
from math import sqrt
#from itertools import permutations as perm
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
    # print(pattern)
    # print(result:=rotate_90(['.#.', '..#', '###']))
    # print(rotate_90(result))
    permutations.append(''.join(list(rows)))
    permutations.append(''.join(rotate_90(list(rows))))
    permutations.append(''.join(rotate_90(rotate_90(list(rows)))))
    permutations.append(''.join(rotate_90(rotate_90(rotate_90(list(rows))))))
    permutations.append(''.join(reflect_x(rotate_90(list(rows)))))
    permutations.append(''.join(reflect_y(rotate_90(list(rows)))))
    permutations.append(''.join(reflect_x(rotate_90(rotate_90(list(rows))))))
    permutations.append(''.join(reflect_y(rotate_90(rotate_90(list(rows))))))
    permutations.append(''.join(reflect_x(rotate_90(rotate_90(rotate_90(list(rows)))))))
    permutations.append(''.join(reflect_y(rotate_90(rotate_90(rotate_90(list(rows)))))))
    permutations.append(''.join(reflect_x(list(rows))))
    permutations.append(''.join(rotate_90(reflect_x(list(rows)))))
    permutations.append(''.join(reflect_y(list(rows))))
    permutations.append(''.join(rotate_90(reflect_y(list(rows)))))
    permutations.append(''.join(reflect_x(reflect_y(list(rows)))))
    permutations.append(''.join(reflect_x(reflect_y(rotate_90(list(rows))))))
    permutations.append(''.join(rotate_90(reflect_x(reflect_y(list(rows))))))
    for perm in permutations:
        patterns[perm] = ''.join(enhancement.strip().split('/'))
#print(patterns)
# ---------------------- Creating patterns  ---------------------- #

#START_PATTERN = "#..#........#..#"
START_PATTERN = ".#...####"


def split_square(square):
    size = int(sqrt(len(square)))
    #squares_per_row = size // 2
    printrow = ""
    #print("------------- SQUARE %d --------------" % size)
    for i in range(1, len(square)+1):
        printrow += square[i-1]
        if (i) % size == 0:
            #print(printrow)
            printrow = ""
    #print("------------- SQUARE --------------")
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
            #print("patterns: ", patterns[new_square])
            #print("subsquares: ", new_square, "pattern match: ", patterns[new_square])
            new_squares.append(patterns[new_square])
    rows = []
    #print("new_squares: ", new_squares, "len new_squares: ", len(new_squares))
    for i in range(0, len(new_squares), layer_squares):
        for j in range(0, len(new_squares[0]), new_square_size):
            row = ""
            for k in range(i, i+layer_squares):
                row += new_squares[k][j:j+new_square_size]
                #print("row: ", row, "k", k)
            rows.append(row)
    new_square = ''.join(rows)
    return new_square

square = START_PATTERN
for _ in range(iterations := 18):
    square = split_square(square)
#print(square)
print("Solution part 1: " + str(list.count(list(square), '#')))
