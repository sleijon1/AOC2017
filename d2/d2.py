lines = open("input.txt").readlines()
diffs = 0

for line in lines:
    row = list(map(int, line.split("\t")))
    diffs += max(row)-min(row)

print("Solution part1: " + str(diffs))

divs = 0
for line in lines:
    row = list(map(int, line.split("\t")))
    for i, number in enumerate(row):
        (new_row := list(row)).remove(number)
        for div in map(lambda x: x/number, new_row):
            if div.is_integer():
                divs += div

print("Solution part 2: " + str(int(divs)))
