lines = open("input.txt").readlines()
lines = list(map(int, lines))

i = 0
steps = 0
while True:
    try:
        next_i = lines[i] + i
    except IndexError:
        print("Escaped maze in: " + str(steps) + " steps.")
        break
    lines[i] += (-1 if lines[i] >= 3 else 1)
    #lines[i] += 1  # Part 1
    i = next_i
    steps += 1
