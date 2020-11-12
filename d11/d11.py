directions = open("input.txt").read().strip()
directions = directions.split(",")
print(directions)

dirs = {
    "n": (0, 2),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -2),
    "sw": (-1, -1),
    "nw": (-1, 1),
}

def hexagonal_distance(a, b) -> int:
    """ Calculates the hexagonal distance between
    two hexagons (a, b) in a hexagonal grid using double height
    """
    diffx = abs(a[0] - b[0])
    diffy = abs(a[1] - b[1])
    distance = diffx + max(0, (diffy - diffx)//2)
    return distance

def calculate_pos(directions) -> (int, int):
    pos = (0, 0)
    max_distance = 0
    for direction in directions:
        dx, dy = dirs[direction][0], dirs[direction][1]
        pos = (pos[0] + dx, pos[1] + dy)
        if (hex_dist := hexagonal_distance((0,0), pos)) > max_distance:
            max_distance = hex_dist
    print("End position: " + str(pos))
    print("Solution part 1: " + str(hexagonal_distance((0,0), pos)))
    print("Solution part 2: " + str(max_distance))

calculate_pos(directions)
