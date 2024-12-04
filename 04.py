data = open('inputs/04.txt').read().split()

dictionary = {}

for i, line in enumerate(data):
    for j,char in enumerate(line):
        dictionary[(i,j)] = char

## Part 1
dirs = [(0,1),(0,-1),(-1,0),(1,0),(-1,1),(-1,-1),(1,1),(1,-1)]

count = 0

for coord in dictionary:
    if dictionary[coord] == "X":
        for dir in dirs:
            position = coord
            for i in range(3):
                position = (position[0] + dir[0], position[1] + dir[1])
                if position not in dictionary:
                    break
                if i == 0 and dictionary[position] != "M":
                    break
                elif i == 1 and dictionary[position] != "A":
                    break
                elif i == 2 and dictionary[position] == "S":
                    count += 1

print(count)

## Part 2
# M.S
# .A.
# M.S

dirs2 = [(1,1),(-1,1),(-1,-1),(1,-1)]

count2 = 0

for coord in dictionary:
    m = 0
    s = 0
    if dictionary[coord] == "A":
        topleft = ""
        bottomright = ""
        for dir in dirs2:
            position = (coord[0] + dir[0], coord[1] + dir[1])
            if position not in dictionary:
                break
            if dictionary[position] == "M":
                m += 1
            if dictionary[position] == "S":
                s +=1
            if dir == (1,1):
                topleft = dictionary[position]
            if dir == (-1,-1):
                bottomright = dictionary[position]
            if m == 2 and s == 2 and topleft != bottomright:
                count2+=1

print(count2)