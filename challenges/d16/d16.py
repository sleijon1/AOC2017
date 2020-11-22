from collections import deque
def dance():
    inp = open("input.txt").read().strip()
    moves = inp.split(',')
    lineup = list(map(chr, range(97, 113))) # part 1 lineup
    last_lineup = None
    for i in range(1000000000):
        for move in moves:
            if move[0] == 's':
                to_move = len(lineup)-int(move[1:])
                dancers_to_move = lineup[:to_move]
                lineup[:to_move] = []
                lineup[len(lineup):] = dancers_to_move
            elif move[0] == 'p':
                ex_1 = lineup[(ind1 := lineup.index(move[1]))]
                ex_2 = lineup[(ind2 := lineup.index(move[3]))]
                lineup[ind1] = ex_2
                lineup[ind2] = ex_1
            elif move[0] == 'x':
                ind1, ind2 = move[1:].split('/')
                ex_1 = lineup[int(ind1)]
                ex_2 = lineup[int(ind2)]
                lineup[int(ind1)] = ex_2
                lineup[int(ind2)] = ex_1
        #print("Solution part 1: " + ''.join(lineup))
        if i % 99 == 0:
            if last_lineup is not None and lineup == last_lineup:
                print("Solution part 2: " + ''.join(lineup))
                break
            else:
                last_lineup = lineup
dance()
