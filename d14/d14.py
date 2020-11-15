import sys
sys.path.append('../')
from d10.d10 import *

inp = "a0c2017"

def hex_to_bin(hex_data):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    bin_data = bin(int(hex_data, scale))[2:].zfill(num_of_bits)
    return bin_data

def produce_hash(inp):
    sparse_hash = knot_hash(inp)
    dense = dense_hash(sparse_hash)
    print(hex_dense(dense))
    HASH = ""
    for digit in hex_dense(dense):
        HASH += digit
    return HASH

def make_grid(INPUT):
    for i in range(0, 128):
        pass

make_grid()
