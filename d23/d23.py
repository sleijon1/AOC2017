from collections import defaultdict
instructions = open('input.txt').read().strip().splitlines()

def run_instructions(registers, ipr=0):
    instruction_ptr = ipr
    multiplications = 0
    while instruction_ptr >= 0 and instruction_ptr < len(instructions):
        instruction = instructions[instruction_ptr]
        print(instruction)
        print(registers['a'])
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
            # elif op == 'add':
            #     registers[reg1] += val
            #     instruction_ptr += 1
            elif op == 'mul':
                registers[reg1] *= val
                instruction_ptr += 1
                multiplications += 1
            elif op == 'sub':
                registers[reg1] -= val
                instruction_ptr += 1
            # elif op == 'mod':
            #     registers[reg1] = registers[reg1] % val
            #     instruction_ptr += 1
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
print(len(registers))
