lines = list(map(int, open("input.txt").read().split("\t")))
observed_states = []
redist_cycle = 1
while True:
    if lines in [state[0] for state in observed_states]:
        print("Solution part 1: " + str(len(observed_states)))
        first_occ_cycle = [state[1] for state in observed_states
                           if state[0] == lines][0]
        print("Solution part 2: " + str(redist_cycle-first_occ_cycle))
        break
    else:
        observed_states.append((list(lines), redist_cycle))
    max_blocks = max(lines)
    reallocate_i = lines.index(max_blocks)
    lines[reallocate_i] = 0
    current = reallocate_i
    for _ in range(max_blocks):
        current = current + 1
        if current > len(lines)-1:
            current -= len(lines)
        lines[current] += 1
    redist_cycle += 1
