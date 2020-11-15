from copy import deepcopy
lines = open("input.txt").readlines()

class Scanner():
    def __init__(self, x, depth):
        self.x = x
        self.y = 0
        self.depth = depth
        self.max_y = self.depth-1
        self.direction = 1

    def __str__(self):
        return str((self.x, self.y, self.direction, self.depth))

    def __repr__(self):
        return str(self)

    def move(self):
        """ swap direction if we are at bottom """
        self.y += self.direction
        if self.y == (self.depth-1):
            self.direction = -1
        elif self.y == 0:
            self.direction = 1

    def dist_from_zero(self):
        if self.direction > 0 and self.y != 0:
            dist_to_bot = self.max_y - self.y
            dist_to_top = self.max_y
        else:
            dist_to_bot = 0
            dist_to_top = self.y
        return dist_to_bot+dist_to_top

    def position_in_steps(self, s):
        """ returns position scanner will be in in s steps"""

        pass


class Packet():
    def __init__(self, x):
        self.x = x
        self.y = 0

    def move(self):
        self.x += 1


def create_scanners():
    scanners = []
    for line in lines:
        x, depth = line.strip().split(": ")
        scanners.append(Scanner(int(x), int(depth)))
    return scanners

def move_packet(scanners):
    packet = Packet(-1)
    severity = []
    for i in range(max([scanner.x for scanner in scanners])+2):
        packet.move()
        for scanner in scanners:
            if packet.x == scanner.x and packet.y == scanner.y:
                severity.append(scanner.x*scanner.depth)
            scanner.move()
    print("Solution part 1: " + str(sum(severity)))


def move_packet_p2(scanners):
    delay = 1
    while True:
        caught = False
        skip_check = False
        for scanner in scanners:
            scanner.move()
            if not skip_check:
                mod = 2*(scanner.depth-1)
                steps = scanner.x % mod
                if steps - scanner.dist_from_zero() == 0:
                    caught = True
                    skip_check = True
        if not caught:
            break
        delay += 1
    print("Solution part 2: " + str(delay))


scanners = create_scanners()
move_packet(deepcopy(scanners))
move_packet_p2(deepcopy(scanners))
