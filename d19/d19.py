lines = open("input.txt").readlines()
grid = []
for line in lines:
    grid.append(list(line.strip('\n')))

def follow_path(grid=grid):
    packet_pos = (grid[0].index('|'), 0) # initial pos
    direction = (0, 1) # starting downwards
    collected_letters = []
    steps = 0
    while True:
        px, py = packet_pos
        dx, dy = direction
        nx, ny = px+dx, py+dy
        try:
            map_item = grid[ny][nx]
            # If new pos does not imply IE we will take a step
            steps += 1
            if map_item == ' ':
                break
            if map_item not in ('-', '|', '+'):
                collected_letters.append(map_item)
            elif map_item == '+' and ((ny+dy == len(grid) or nx+dx == len(grid[0]))
                                      or (grid[ny+dy][nx+dx] == ' ')):
                left_right = [((1, 0), nx+1, ny), ((-1, 0), nx-1, ny)]
                down_up = [((0, 1), nx, ny+1), ((0, -1), nx, ny-1)]
                if direction in ((0, 1), (0, -1)):
                    to_check = left_right
                else:
                    to_check = down_up
                for move in to_check:
                    d, adjx, adjy = move
                    if adjy < len(grid) and adjx < len(grid[0]):
                        if grid[adjy][adjx] != ' ':
                            direction = d
            packet_pos = (nx, ny)
        except IndexError:
            break
    print("Solution part 1: " + str(''.join(collected_letters)))
    print("Solution part 2: " + str(steps))
follow_path(grid)
