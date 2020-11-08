import re
lines = open("input.txt").readlines()

all_children = {}
parents = []
weights = {}
for line in lines:
    if "->" in line:
        parent, weight, _ = line.split("->")[0].split(" ")
        weights[parent] = int(weight.strip("\n\(\)"))
        parents.append(parent)
        children = line.split("->")[1].split(",")
        for i, child in enumerate(children):
            children[i] = child.strip(" ,\n")
        all_children[parent] = children
    else:
        child, weight = line.split("->")[0].split(" ")
        weights[child] = int(weight.strip("\n\(\)"))

for parent in parents:
    oldest_parent = True
    for siblings in all_children.values():
        if parent in siblings:
            oldest_parent = False
            break
    if oldest_parent:
        print("Solution part 1: " + str(parent))
        break

def find_weight(parent):
    """ recursively finds the nodes where
    sibling weight differs
    """
    try:
        children = all_children[parent]
    except KeyError:
        return weights[parent]
    child_weights = []
    for child in children:
        c_weight = find_weight(child)
        if c_weight is None:
            # Only happens when we find a bad weight
            return
        child_weights.append(c_weight)
    if len(set(child_weights)) > 1:
        # break program
        differing_weights = set(child_weights)
        unique_weight = [(weight, i)
                         for i, weight in enumerate(child_weights)
                         if weight not in
                         [w for j, w in enumerate(child_weights) if i != j]][0]
        print("Bad weight: " + str(weights[children[unique_weight[1]]]) + ". Belonging to " + \
              str(children[unique_weight[1]]))
        print("Adjust by (+-): " +
              str(abs(differing_weights.pop()-differing_weights.pop())))
        print("Non-matching weights: " + str(child_weights))
        print("Belonging to children: " + str(children))
        return
    return sum(child_weights) + weights[parent]


find_weight("cqmvs")
