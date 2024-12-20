from collections import defaultdict

data = open('data/12-1.txt', 'r').read().split('\n')

col_1, col_2 = [], []

for row in data:
    d1, d2 = row.split()
    col_1.append(int(d1))
    col_2.append(int(d2))

## part 1 ##
col_1.sort()
col_2.sort()

print(sum(map(lambda data :  abs(data[0]-data[1]), zip(col_1, col_2))))

col_2_map = defaultdict(lambda : 0)

## part 2 ##
for num in col_2:
    col_2_map[num] = col_2_map[num] + 1

print(sum(map(lambda x : x*col_2_map[x], col_1)))