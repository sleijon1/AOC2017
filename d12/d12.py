lines = open("input.txt").readlines()

pipes = {}

for line in lines:
    line.strip()
    startp, endp = line.split("<->")
    startp = int(startp)
    pipes[startp] = []
    for p in map(int, endp.split(", ")):
        pipes[int(startp)].append(p)


# def count_group():
#     zero_com = set()
#     for zcom in pipes[0]:
#         zero_com.add(zcom)
#     # fun brute force way of finding all possible
#     # ids in coms with 0
#     for i in range(1, 21):
#         for start in pipes:
#             if start in zero_com:
#                 for end in pipes[start]:
#                     zero_com.add(end)
#     print(zero_com)
#     print("Solution part 1: " + str(len(zero_com)))


def count_group():
    groups = []
    for pipe in pipes:
        skip = False
        for group in groups:
            if pipe in group:
                skip = True
                break
        if skip:
            continue
        groups.append(create_group(pipe, set()))
    print("Solution part 1: " + str(len(groups[0])))
    print("Solution part 2: " + str(len(groups)))

def create_group(startp, group):
    group.add(startp)
    for ID in pipes[startp]:
        if ID in group:
            continue
        create_group(ID, group)
    return group


count_group()
