from itertools import permutations

class NonValidPass(Exception):
    # For breaking out of loop
    pass

lines = open("input.txt").readlines()
# fun one-liner for part 1
# valid = sum([1 for line in lines
#              if len(line.strip().split(" ")) ==
#              len(set(line.strip().split(" ")))])

valid = 0
for line in lines:
    passphrase = line.strip().split(" ")
    if len(set(passphrase)) == len(passphrase):
        valid += 1

print("Solution part 1: " + str(valid))

non_valid_pass = NonValidPass()
valid = 0
for line in lines:
    passphrase = line.strip().split(" ")
    # first requirement
    if len(set(passphrase)) != len(passphrase):
        continue

    # second requirement
    # there may not be two words in
    # the same group of permutations
    perms = permutations(passphrase[0])
    try:
        for word in passphrase:
            perms = permutations(word)
            for perm in perms:
                if ''.join(perm) in passphrase and ''.join(perm) != word:
                    raise non_valid_pass
    except NonValidPass:
        continue
    valid += 1

print("Solution part 2: " + str(valid))
