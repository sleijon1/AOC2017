import re
from copy import deepcopy
particles = open("input.txt").readlines()

positions = []
velocities = []
accelerations = []

for particle in particles:
    x, y, z, dx, dy, dz, ax, ay, az = map(int, re.findall('-?\d+', particle.strip('\n')))
    positions.append([x, y, z])
    velocities.append([dx, dy, dz])
    accelerations.append([ax, ay, az])
part1pos = deepcopy(positions)
part1vel = deepcopy(velocities)
part1acc = deepcopy(accelerations)
for _ in range(500):
    for pos, vel, acc in zip(part1pos, part1vel, part1acc):
        for i in range(3):
            vel[i] += acc[i]
            pos[i] += vel[i]
mh_dist = [sum([abs(axis) for axis in pos]) for pos in part1pos]
particle_closest_zero = mh_dist.index(min(mh_dist))
print("Solution part 1: " + str(particle_closest_zero))

for _ in range(150):
    for pos in positions:
        count = positions.count(pos)
        if count > 1:
            for _ in range(count):
                index = positions.index(pos)
                positions.pop(index)
                velocities.pop(index)
                accelerations.pop(index)
    for pos, vel, acc in zip(positions, velocities, accelerations):
        for i in range(3):
            vel[i] += acc[i]
            pos[i] += vel[i]
print("Solution part 2: " + str(len(positions)))
