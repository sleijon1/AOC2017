from collections import defaultdict, deque
instructions = open('input.txt').read().strip().splitlines()

def run_instructions(registers, ipr=0, received=deque([]), part1=False):
    instruction_ptr = ipr
    sound_played = None
    send = deque([])
    while instruction_ptr >= 0 and instruction_ptr < len(instructions):
        instruction = instructions[instruction_ptr]
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
            elif op == 'add':
                registers[reg1] += val
                instruction_ptr += 1
            elif op == 'mul':
                registers[reg1] *= val
                instruction_ptr += 1
            elif op == 'mod':
                registers[reg1] = registers[reg1] % val
                instruction_ptr += 1
            elif op == 'jgz':
                try:
                    reg1 = int(reg1)
                except ValueError:
                    reg1 = registers[reg1]
                if reg1 > 0:
                    instruction_ptr += val
                else:
                    instruction_ptr += 1
        else:
            op, reg1 = instruction.split(" ")
            if op == 'snd':
                try:
                    reg1 = int(reg1)
                except ValueError:
                    reg1 = registers[reg1]
                sound_played = reg1
                send.appendleft(reg1)
            elif op == 'rcv':
                if part1:
                    if registers[reg1] > 0:
                        print("Solution part 1: " + str(sound_played))
                        return sound_played
                        break
                if not received:
                    return send, instruction_ptr
                else:
                    registers[reg1] = received.pop()

            instruction_ptr += 1
    return send, instruction_ptr
registers = defaultdict(int)
assert(run_instructions(registers, part1=True) == 1187)

registers0 = defaultdict(int)
registers1 = defaultdict(int)
registers0['p'] = 0
registers1['p'] = 1
def run_both():
    ipr0 = ipr1 = 0
    send0 = []
    send1 = []
    sent1 = 0
    while True:
        send0, ipr0 = run_instructions(registers0, ipr0, send1)
        send1, ipr1 = run_instructions(registers1, ipr1, send0)
        sent1 += len(send1)
        if not send0 and not send1:
            print("Solution part 2: " + str(sent1))
            break

run_both()
