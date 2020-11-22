side = 1
counter = 0
layers = []
layer = 0
current_layer = []

def square(xy, length, number):
    # each square follows the same coordinate pattern
    # with different length depending on which layer it is
    for y in range(-length+1, length+1): # +1 for range exclusive
        xy[(length, y)] = number
        number += 1
    for x in range(-length+1, length+1):
        xy[(-x, length)] = number
        number += 1
    for y in range(-length+1, length+1):
        xy[(-length, -y)] = number
        number += 1
    for x in range(-length+1, length+1):
        xy[(x, -length)] = number
        number += 1
    return number

def squares():
    xy = {}
    layer = 1
    number = 2
    while True:
        number = square(xy, layer, number)
        layer += 1
        if 277678 in xy.values():
            # We counted up to 277678
            break
    print("Solution part 1: " + str([abs(key[0]) + abs(key[1])
                                     for key, value in xy.items()
                                     if value == 277678][0]))
    # Reset all values for part 2
    xy = {key: 0 for key in xy}
    xy[(0, 0)] = 1
    # Set values
    for (x, y) in xy:
        adj_sum = 0
        # include (x, y) so we don't have to care for special case
        # since xy[(x, y)] is always zero when setting its value
        adjacent = [(x, y), (x-1, y), (x, y-1), (x-1, y-1), (x+1, y),
                    (x+1, y+1), (x, y+1), (x+1, y-1), (x-1, y+1)]
        for adj in adjacent:
            adj_sum += xy[adj]
        xy[x, y] = adj_sum

        if adj_sum > 277678:
            print("Solution part 2: " + str(adj_sum))
            exit()


squares()
