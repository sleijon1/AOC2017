from collections import defaultdict
instructions = open('input.txt').read().strip().splitlines()
registers = defaultdict(int)

instruction_ptr = 0
sound_played = None
while instruction_ptr >= 0 and instruction_ptr < len(instructions):
    instruction = instructions[instruction_ptr]
    #print(instruction_ptr)
    #print("reg a:", registers['a'])
    try:
        op, reg1, val = instruction.split(" ")
        try:
            val = int(val)
            registers[val] = val
        except ValueError:
            pass
        if op == 'set':
            registers[reg1] = registers[val]
            instruction_ptr += 1
        elif op == 'add':
            registers[reg1] += registers[val]
            instruction_ptr += 1
        elif op == 'mul':
            registers[reg1] *= registers[val]
            instruction_ptr += 1
        elif op == 'mod':
            registers[reg1] = registers[reg1] % registers[val]
            instruction_ptr += 1
        elif op == 'jgz':
            if registers[reg1] > 0:
                instruction_ptr += registers[val]
            else:
                instruction_ptr += 1
    except ValueError:
        op, reg1 = instruction.split(" ")
        if op == 'snd':
            sound_played = registers[reg1]
        elif op == 'rcv':
            if registers[reg1] > 0:
                print("Solution part 1: " + str(sound_played))
                break
        instruction_ptr += 1
