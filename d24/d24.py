from copy import deepcopy


lines = open("input.txt").readlines()
bridges = []
for line in lines:
    bridge = tuple(map(int, line.strip().split('/')))
    bridge = sorted(bridge)
    bridges.append(bridge)


def find_strongest(bridges):
    queue = [(bridge, 1, []) for bridge in bridges if bridge[0] == 0]
    valid_bridges = []
    while queue:
        current_bridge, open_index, path = queue.pop(0)
        copy_path = deepcopy(path)
        copy_path.append(current_bridge)
        #print("Current bridge:", current_bridge)
        #print("Current open index:", open_index)
        possible_connections = [bridge for bridge in bridges
                                if current_bridge[open_index] in bridge
                                and current_bridge != bridge
                                and bridge not in path]
        for connection in possible_connections:
            new_open_index = None
            if connection.index(current_bridge[open_index]) == 1:
                new_open_index = 0
            elif connection.index(current_bridge[open_index]) == 0:
                new_open_index = 1
            queue.append((connection, new_open_index, copy_path))
        valid_bridges.append(copy_path)
        #print("Possible connections:", possible_connections)
        #print("Queue:", queue)
    strongest = 0
    max_path = None
    for bridge in valid_bridges:
        total = sum([connection[0] + connection[1]
                     for connection in bridge])
        if total > strongest:
            strongest = total
            max_path = bridge
    print("Solution part 1: " + str(strongest))
    print(max_path)
    max_length = max([len(bridge) for bridge in valid_bridges])
    max_length_bridges = [bridge for bridge in valid_bridges
                          if len(bridge) == max_length]
    strongest = 0
    for bridge in max_length_bridges:
        total = sum([connection[0] + connection[1]
                     for connection in bridge])
        if total > strongest:
            strongest = total
    print("Solution part 2: " + str(strongest))


find_strongest(bridges)
