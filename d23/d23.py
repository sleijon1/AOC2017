from collections import defaultdict
instructions = open('input.txt').read().strip().splitlines()

def run_instructions(registers, ipr=0):
    instruction_ptr = ipr
    multiplications = 0
    while instruction_ptr >= 0 and instruction_ptr < len(instructions):
        instruction = instructions[instruction_ptr]
        # For seeing where it gets stuck
        # print(instruction)
        # print("g:", registers['g'])
        # print("h:", registers['h'])
        # print("b:", registers['b'])
        # print("d:", registers['d'])
        # print("f:", registers['f'])
        # print("c:", registers['c'])
        # print("e:", registers['e'])
        if len(instruction.split(" ")) == 3:
            op, reg1, val = instruction.split(" ")
            try:
                val = int(val)
            except ValueError:
                val = registers[val]
                pass
            if op == 'set':
                registers[reg1] = val
                instruction_ptr += 1
            elif op == 'mul':
                registers[reg1] *= val
                instruction_ptr += 1
                multiplications += 1
            elif op == 'sub':
                registers[reg1] -= val
                instruction_ptr += 1
            elif op == 'jnz':
                try:
                    reg1 = int(reg1)
                except ValueError:
                    reg1 = registers[reg1]
                if reg1 != 0:
                    instruction_ptr += val
                else:
                    instruction_ptr += 1
    print("Solution part 1: " + str(multiplications))


registers = defaultdict(int)
run_instructions(registers)

""" Reverse engineer of what the program does
counts how many times register b is not a prime number
"""
init_b = 106500
c = 106500+17000
h = 0
for b in range(init_b, c+17, 17):
    for d in range(2, b):
        if b % d == 0:
            h += 1
            break
print("Solution part 2: " + str(h))
