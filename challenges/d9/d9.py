stream = open("input.txt").read().strip()
print(stream)
def count_groups():
    garbage = False
    opened_groups = 0
    closed_groups = 0
    scores = []
    skip_next = False
    garbage_counter = 0
    for i, char in enumerate(stream):
        if skip_next:
            skip_next = False
        elif char == "!":
            skip_next = True
        elif char == "<" and not garbage:
            garbage = True
        elif char == ">" and garbage:
            garbage = False
        elif char == "{" and not garbage:
            opened_groups += 1
        elif char == "}" and not garbage:
            if opened_groups > 0:
                scores.append(opened_groups)
                opened_groups -= 1
        elif garbage:
            garbage_counter += 1

    print("Solution part 1: " + str(scores) + " | sum = " + str(sum(scores)))
    print("Solution part 2, amount of garbage: " + str(garbage_counter))

count_groups()
