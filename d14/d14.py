import sys
sys.path.append('../')
from d10.d10 import *

inp = "a0c2017"


def hex_to_bin(hex_data):
    scale = 16  # equals to hexadecimal
    num_of_bits = 4
    bin_data = bin(int(hex_data, scale))[2:].zfill(num_of_bits)
    return bin_data


def produce_hash(inp):
    sparse_hash = knot_hash(inp)
    dense = dense_hash(sparse_hash)
    HASH = ""
    for digit in hex_dense(dense):
        HASH += digit
    return HASH


def make_grid(INPUT):
    used = 0
    grid = []
    for i in range(0, 128):
        row = ""
        curr_hash = produce_hash(INPUT+'-'+str(i))
        for char in curr_hash:
            bin_hash = hex_to_bin(char)
            bin_hash = ''.join(['#' if dig == '1' else '.' for dig in bin_hash])
            used += bin_hash.count('#')
            row += bin_hash
        grid.append(list(row))
    print("Solution part 1: " + str(used))
    return grid


def count_regions(grid):
    current_region = 1
    for j, row in enumerate(grid):
        for i, square in enumerate(row):
            if square != '#':
                continue
            (queue := list()).append((i, j))
            while queue:
                curr_x, curr_y = queue.pop(0)
                grid[curr_y][curr_x] = current_region
                adjacent = [(curr_x-1, curr_y), (curr_x, curr_y-1),
                            (curr_x+1, curr_y), (curr_x, curr_y+1)]
                for x, y in adjacent:
                    if y >= 0 and y < 128 and x >= 0 and x < 128:
                        if grid[y][x] == '#':
                            queue.append((x, y))
            current_region += 1
    total_regions = current_region - 1 # last cr += 1 doesnt amount to a region
    print("Solution part 2: " + str(total_regions))


grid = make_grid('hfdlxzhv')
count_regions(grid)
