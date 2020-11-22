from collections import defaultdict
lines = open("input.txt").readlines()
comparisons = {
    '<' : lambda x, y: True if x < y else False,
    '<=' : lambda x, y: True if x <= y else False,
    '>' : lambda x, y: True if x > y else False,
    '>=' : lambda x, y: True if x >= y else False,
    '==' : lambda x, y: True if x == y else False,
    '!=' : lambda x, y: True if x != y else False,
}

registers = defaultdict(int)  # default value 0

def add_sign(sign, num):
    return (-1*num if sign == "dec" else num)

max_value = 0
for line in lines:
    modify, sign, amount, _, cmp_reg, comparison, num = line.strip().split(" ")
    if comparisons[comparison](registers[cmp_reg], int(num)):
        registers[modify] += add_sign(sign, int(amount))
        if registers[modify] > max_value:
            max_value = registers[modify]
print("Solution part 1: " + str(max(registers.values())))
print("Solution part 2: " + str(max_value))
