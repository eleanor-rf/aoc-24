import numpy as np

data = np.loadtxt("inputs/01.txt", dtype=int)

left_list, right_list = np.sort(data[:, 0]), np.sort(data[:, 1])

## Part 1
solution_p1 = np.sum(np.abs(left_list - right_list))

print("The sum of differences is", solution_p1)

## Part 2
solution_p2 = np.sum(np.array(np.bincount(right_list)[left_list]) * left_list)

print("The similarity score is", solution_p2)