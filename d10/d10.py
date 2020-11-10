import re
#lengths = [197, 97, 204, 108, 1, 29, 5, 71, 0, 50, 2, 255, 248, 78, 254, 63]
lengths = "1,2,3"
new_lengths = []
for num in map(ord, re.findall(r'\d+', lengths)):
    new_lengths.append(num)
    new_lengths.append(ord(','))
new_lengths = new_lengths[0:-1] + [17, 31, 73, 47, 23]
print(new_lengths)
exit()
string = [num for num in range(256)]
# lengths = [3, 4, 1, 5]
# string = [num for num in range(5)]

def knot_hash(rounds=64):
    for _ in range(rounds):
        skip_size = 0
        position = 0
        for length in lengths:
            if length + position < len(string):
                list.reverse(rev_slice := string[position:position + length])
                string[position:position + length] = rev_slice
            else:
                reverse1 = string[position:]
                wrap_around = ((position+length) % len(string))
                reverse2 = string[:wrap_around]
                reverse = reverse1 + reverse2
                list.reverse(reverse)
                string[position:] = reverse[:len(string[position:])]
                string[:wrap_around] = reverse[len(string[position:]):]

            position = (skip_size + length + position) % len(string)
            skip_size += 1

    #print("Solution part 1: " + str(string[0] * string[1]))

knot_hash()
