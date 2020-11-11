import re
from functools import reduce
#lengths = [197, 97, 204, 108, 1, 29, 5, 71, 0, 50, 2, 255, 248, 78, 254, 63] # Part 1
lengths = "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"
lengths = [ord(char) for char in lengths]
lengths = lengths + [17, 31, 73, 47, 23]
string = [num for num in range(256)]
# lengths = [3, 4, 1, 5]
# string = [num for num in range(5)]

def knot_hash(rounds=64):
    skip_size = 0
    position = 0
    for _ in range(rounds):
        for length in lengths:
            if length + position < len(string):
                list.reverse(rev_slice := string[position:position + length])
                string[position:position + length] = rev_slice
            else:
                reverse1 = string[position:]
                wrap_around = ((position+length) % len(string))
                reverse2 = string[:wrap_around]
                reverse = reverse1 + reverse2
                list.reverse(reverse)
                string[position:] = reverse[:len(string[position:])]
                string[:wrap_around] = reverse[len(string[position:]):]

            position = (skip_size + length + position) % len(string)
            skip_size += 1
    return string
    #print("Solution part 1: " + str(string[0] * string[1]))

def dense_hash(sparse, block_size=16):
    dense = []
    for i in range(0, len(sparse), block_size):
        block = sparse[i:i+block_size]
        dense.append(reduce(lambda x,y: x^y, block))
    return dense

sparse_hash = knot_hash()
dense = dense_hash(sparse_hash)
hex_dense = ['0' + hex(num).lstrip("0x") if
             len(hex(num).lstrip("0x")) < 2
             else hex(num).lstrip("0x")
             for num in dense]

HASH = ""
for digit in hex_dense:
    HASH += digit
print("Solution part 2, Knot Hash: " + str(HASH))
print(len(HASH))
#print(sparse_hash)
