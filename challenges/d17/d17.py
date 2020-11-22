c_buffer = [0]
current = 1
end_value = 2017
step_size = 328
position = 0
while current < 2018:
    index = (position + step_size) % len(c_buffer)
    c_buffer.insert(index+1, current)
    position = index+1
    current += 1
print("Solution part 1: " + str(c_buffer[c_buffer.index(2017)+1]))

# Don't actually have to
# insert anything since 0 never moves
len_buffer = 1
current = 1
end_value = 2017
step_size = 328
position = 0
value_after_zero = None
while current < 50000001:
    index = (position + step_size) % len_buffer
    len_buffer += 1
    if index+1 == 1:
        value_after_zero = current
    position = index+1
    current += 1
print("Solution part 2: " + str(value_after_zero))
