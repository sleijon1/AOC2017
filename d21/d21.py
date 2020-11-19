lines = open("test.txt").readlines()
for line in lines:
    pattern, enhancement = line.split('=>')
    print(pattern)
start_pattern = ".#...####"
