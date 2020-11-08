f = open("input.txt").read().strip()
digits = f
matching = 0
jump = len(digits)//2
for i in range(len(digits)):
    matching_i = i + jump
    print(digits[i])
    if matching_i > len(digits)-1:
        matching_i = matching_i - len(digits)
    if digits[i] == digits[matching_i]:
        matching += int(digits[i])

print("Part 2: " + str(matching))
