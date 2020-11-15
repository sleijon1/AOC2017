def generator_A(previous):
    factor = 16807
    return (previous*factor) % 2147483647

def generator_B(previous):
    factor = 48271
    return (previous*factor) % 2147483647


def part_one():
    previous_a = 116
    previous_b = 299
    matches = 0
    for i in range(40000000):
        previous_a = generator_A(previous_a)
        previous_b = generator_B(previous_b)
        #print(previous_a, previous_b)
        #print(bin(previous_a), bin(previous_b))
        binary_a = bin(previous_a)
        binary_b = bin(previous_b)
        bin_a = binary_a[-1:-17:-1]
        bin_b = binary_b[-1:-17:-1]
        if len(binary_a) > 18 and len(binary_b) > 18:
            if bin_a == bin_b:
                matches += 1
        # if i == 4:
        #     print(matches)
        #     exit()
    print("Solution part 1: " + str(matches))

def part_two():
    previous_a = 116
    previous_b = 299
    matches = 0
    a_values = []
    b_values = []

    while len(a_values) < 5000000 or len(b_values) < 5000000:
        previous_a = generator_A(previous_a)
        previous_b = generator_B(previous_b)
        if previous_a % 4 == 0:
            binary_a = bin(previous_a)
            bin_a = binary_a[-1:-17:-1]
            a_values.append(bin_a)
        if previous_b % 8 == 0:
            binary_b = bin(previous_b)
            bin_b = binary_b[-1:-17:-1]
            b_values.append((bin_b))
    for a, b in zip(a_values, b_values):
        if len(a) == 16 and len(b) == 16:
            if a == b:
                matches += 1
    print("Solution part 2: " + str(matches))


part_two()
