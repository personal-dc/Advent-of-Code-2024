from collections import defaultdict

data = open('data/12-8.txt', 'r').read().strip().split('\n')

data = [list(d) for d in data]

## part 1 ##

r_max, c_max = len(data), len(data[0])

towers = defaultdict(list)

for r in range(r_max):
    for c in range(c_max):
        char = data[r][c]
        if char != '.' : towers[char].append((r, c))

antinodes = set()

for _, locs in towers.items():
    num_t = len(locs)

    if num_t == 1: break

    for t_1 in range(num_t):
        for t_2 in range(t_1+1, num_t):
            t1_r, t1_c = locs[t_1]
            t2_r, t2_c = locs[t_2]

            diff_r, diff_c = t1_r-t2_r, t1_c - t2_c

            pot_anti1_x, pot_anti1_y = t1_r + diff_r, t1_c + diff_c
            pot_anti2_x, pot_anti2_y = t2_r - diff_r, t2_c - diff_c

            if 0 <= pot_anti1_x <= r_max - 1 and 0 <= pot_anti1_y <= c_max - 1 : antinodes.add((pot_anti1_x, pot_anti1_y))
            if 0 <= pot_anti2_x <= r_max - 1 and 0 <= pot_anti2_y <= c_max - 1 : antinodes.add((pot_anti2_x, pot_anti2_y))

print(len(antinodes))

## part 2 ##

r_max, c_max = len(data), len(data[0])

towers = defaultdict(list)

for r in range(r_max):
    for c in range(c_max):
        char = data[r][c]
        if char != '.' : towers[char].append((r, c))

new_antinodes = set()

for _, locs in towers.items():
    num_t = len(locs)

    if num_t == 1: break

    for t_1 in range(num_t):
        for t_2 in range(t_1+1, num_t):
            
            t1_r, t1_c = locs[t_1]
            t2_r, t2_c = locs[t_2]

            diff_r, diff_c = t1_r-t2_r, t1_c - t2_c

            pos_r, pos_c = t2_r, t2_c

            while 0 <= pos_r <= r_max - 1 and 0 <= pos_c <= c_max - 1:
                new_antinodes.add((pos_r, pos_c))

                pos_r, pos_c = pos_r + diff_r, pos_c + diff_c

            pos_r, pos_c = t2_r, t2_c

            while 0 <= pos_r <= r_max - 1 and 0 <= pos_c <= c_max - 1:
                new_antinodes.add((pos_r, pos_c))

                pos_r, pos_c = pos_r - diff_r, pos_c - diff_c


print(len(new_antinodes))
