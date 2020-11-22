steps = 12861455
state = 'A'
cursor = round(steps/2)
tape = [0 for _ in range(steps)]
for _ in range(steps):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
        else:
            tape[cursor] = 0
            cursor -= 1
        state = 'B'
    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        else:
            tape[cursor] = 0
            cursor += 1
            state = 'E'
    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'E'
        else:
            tape[cursor] = 0
            cursor -= 1
            state = 'D'
    elif state == 'D':
        tape[cursor] = 1
        cursor -= 1
        state = 'A'
    elif state == 'E':
        if tape[cursor] == 0:
            state = 'A'
        else:
            state = 'F'
        tape[cursor] = 0
        cursor += 1
    elif state == 'F':
        if tape[cursor] == 0:
            state = 'E'
        else:
            state = 'A'
        tape[cursor] = 1
        cursor += 1

print("Solution part 1: " + str(tape.count(1)))
