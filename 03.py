from re import findall

data = open('inputs/03.txt').read()
data = 'do()' + data + 'don\'t()'

## Part 1
matches = findall(r'mul\(\d+,\d+\)', data)

def calculate_sum(matches):
    total_sum = 0
    for match in matches:
        nums = findall(r'\d+', match)
        mult = int(nums[0]) * int(nums[1])
        total_sum += mult
    return total_sum

print("Sum for part 1:", calculate_sum(matches))

## Part 2
cond_matches = findall(r"do\(\)([\s\S]*?)don't\(\)", data)

cond_sum = 0
for match in cond_matches:
    muls = findall(r'mul\(\d+,\d+\)', match)
    cond_sum += calculate_sum(muls)

print("Sum for part 2:", cond_sum)