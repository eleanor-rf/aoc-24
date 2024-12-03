import numpy as np

data = []

with open("inputs/02.txt", 'r') as file:
    for line in file:
        row = np.array(list(map(int, line.split())))
        data.append(row)

## Part 1
def is_safe(array):
    steps = np.diff(array)
    signs = np.sign(steps)
    return (np.all(np.abs(steps) <= 3) and np.all(np.abs(steps) != 0)) and np.all(signs == signs[0])

safe_list = []
unsafe_list = []
for level in data:
    if is_safe(level):
        safe_list.append(level)
    else:
        unsafe_list.append(level)

print("Number of safe sequences for part 1:", len(safe_list))

## Part 2
for level in unsafe_list:
    for i in range(len(level)):
        modified_list = np.delete(level,i)
        if is_safe(modified_list):
            safe_list.append(level)
            break

print("Number of safe sequences for part 2:", len(safe_list))