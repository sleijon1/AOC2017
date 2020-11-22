from collections import deque
lines = open("input.txt").readlines()

INFECTED = '#'
CLEAN = '.'
FLAGGED = 'F'
WEAKENED = 'W'
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
EAST = (1, 0)


class Virus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = SOUTH
        self.infected = 0

    def move(self, grid):
        turn = None
        if grid[self.y][self.x] == INFECTED:
            turn = EAST
            grid[self.y][self.x] = FLAGGED
        elif grid[self.y][self.x] == CLEAN:
            grid[self.y][self.x] = WEAKENED
            turn = WEST
        elif grid[self.y][self.x] == WEAKENED:
            grid[self.y][self.x] = INFECTED
            self.infected += 1
        elif grid[self.y][self.x] == FLAGGED:
            grid[self.y][self.x] = CLEAN
            if self.direction == WEST:
                self.direction = EAST
            elif self.direction == EAST:
                self.direction = WEST
            elif self.direction == SOUTH:
                self.direction = NORTH
            elif self.direction == NORTH:
                self.direction = SOUTH
        if turn is None:
            pass
        elif self.direction == SOUTH:
            self.direction = turn
        elif self.direction == NORTH and turn == WEST:
            self.direction = EAST
        elif self.direction == NORTH and turn == EAST:
            self.direction = WEST
        elif self.direction == WEST and turn == WEST:
            self.direction = NORTH
        elif self.direction == WEST and turn == EAST:
            self.direction = SOUTH
        elif self.direction == EAST and turn == EAST:
            self.direction = NORTH
        elif self.direction == EAST and turn == WEST:
            self.direction = SOUTH
        self.x, self.y = self.x+self.direction[0], self.y + self.direction[1]

    def __str__(self):
        return str((self.x, self.y))


grid = deque([])
extra = 200
for line in lines:
    line = deque((line.strip()))
    for _ in range(extra):
        line.appendleft('.')
        line.append('.')
    grid.append(line)
for _ in range(extra):
    grid.append(['.' for _ in range(len(grid[0]))])
    grid.appendleft(['.' for _ in range(len(grid[0]))])
center_y = (len(grid)-1)//2
center_x = len(grid[center_y])//2
virus = Virus(center_x, center_y)
bursts = 10000000
for _ in range(bursts):
    virus.move(grid)
print("Solution part 2: " + str(virus.infected))
