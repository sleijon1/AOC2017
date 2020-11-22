import re
from functools import reduce

def knot_hash(lengths, rounds=64):
    skip_size = 0
    position = 0
    lengths = [ord(char) for char in lengths]
    lengths = lengths + [17, 31, 73, 47, 23]
    string = [num for num in range(256)]
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

def dense_hash(sparse, block_size=16):
    dense = []
    for i in range(0, len(sparse), block_size):
        block = sparse[i:i+block_size]
        dense.append(reduce(lambda x,y: x^y, block))
    return dense

def hex_dense(dense_hash):
    hex_dense = []
    for num in dense_hash:
        HEX = hex(num)
        if len(HEX.lstrip('0x')) == 0:
            hex_dense.append('00')
        elif len(HEX.lstrip('0x')) < 2:
            hex_dense.append('0' + HEX.lstrip('0x'))
        else:
            hex_dense.append(HEX.lstrip('0x'))
    return hex_dense

if __name__ == '__main__':
    inp = "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"
    sparse_hash = knot_hash(inp)
    dense = dense_hash(sparse_hash)
    hex_dense = hex_dense(dense)
    HASH = ""
    for digit in hex_dense:
        HASH += digit
    print("Solution part 2, Knot Hash: " + str(HASH))
