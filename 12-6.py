import copy
from sys import get_coroutine_origin_tracking_depth


data = open('data/12-6.txt', 'r').read().strip().split('\n')
data = [list(d) for d in data]

## part 1 ##
escaped = False

# 2-tuple of (x, y)
guard_posn = None
guard_dir = None

x_max, y_max = len(data), len(data[0])

for r in range(x_max):
    for c in range(y_max):
        char = data[r][c]

        if char == '^': 
            guard_posn = (r, c)
            guard_dir = char
            data[r][c] = 'X'
            break


while not escaped:
    x, y = guard_posn

    if guard_dir == '^':
        
        if x-1 < 0:
            escaped = True
            data[x][y] = 'X'
            break

        if data[x-1][y] == '#':
            guard_dir = '>'
        
        else:
            data[x][y] = 'X'
            guard_posn = (x-1, y)

    elif guard_dir == '>':
        
        if y+1 > y_max - 1:
            escaped = True
            data[x][y] = 'X'
            break

        if data[x][y+1] == '#':
            guard_dir = 'v'
        
        else:
            data[x][y] = 'X'
            guard_posn = (x, y+1)

    elif guard_dir == '<':
        
        if y-1 < 0:
            escaped = True
            data[x][y] = 'X'
            break

        if data[x][y-1] == '#':
            guard_dir = '^'
        
        else:
            data[x][y] = 'X'
            guard_posn = (x, y-1)

    elif guard_dir == 'v':
        
        if x+1 > x_max - 1:
            escaped = True
            data[x][y] = 'X'
            break

        if data[x+1][y] == '#':
            guard_dir = '<'
        
        else:
            data[x][y] = 'X'
            guard_posn = (x+1, y)

guard_posn = sum(map(lambda lst : len(list(filter(lambda x : x == 'X', lst))), data))

print(guard_posn)

## part 2 ##

data = open('data/12-6.txt', 'r').read().strip().split('\n')
data = [list(d) for d in data]

# 2-tuple of (x, y)
orig_guard_posn = None
orig_guard_dir = None

x_max, y_max = len(data), len(data[0])

for r in range(x_max):
    for c in range(y_max):
        char = data[r][c]

        if char == '^': 
            orig_guard_posn = (r, c)
            orig_guard_dir = char
            break

def guard_loops(obst_r, obst_c):
    
    guard_posn, guard_dir = copy.deepcopy(orig_guard_posn), copy.deepcopy(orig_guard_dir)
    new_data = open('data/12-6.txt', 'r').read().strip().split('\n')
    new_data = [list(d) for d in new_data]
    new_data[obst_r][obst_c] = '#'
    escaped = False
    loop = False

    ## add some notion of direction to visited cells
    while not (escaped or loop):
        x, y = guard_posn
        assert(new_data[x][y] != '#')
        
        if guard_dir == '^':
            
            if x-1 < 0:
                escaped = True
                new_data[x][y] = 'X'
                break

            if new_data[x-1][y] == '#':
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_dir = '>'
                
            
            elif (len(new_data[x-1][y]) == 2 and 
                  guard_dir in new_data[x-1][y][1]):
                # path.append((x, y))
                loop = True
                break
            
            else:
                # path.append((x, y))
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_posn = (x-1, y)

        elif guard_dir == '>':
            
            if y+1 > y_max - 1:
                escaped = True
                new_data[x][y] = 'X'
                break

            if new_data[x][y+1] == '#':
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_dir = 'v'
                

            elif (len(new_data[x][y+1]) == 2 and 
                  guard_dir in new_data[x][y+1][1]):
                # path.append((x, y))
                loop = True
                break
            
            else:
                # path.append((x, y))
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_posn = (x, y+1)

        elif guard_dir == '<':
            
            if y-1 < 0:
                escaped = True
                new_data[x][y] = 'X'
                break

            if new_data[x][y-1] == '#':
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_dir = '^'
                

            elif (len(new_data[x][y-1]) == 2 and 
                  guard_dir in new_data[x][y-1][1]):
                # path.append((x, y))
                loop = True
                break
            
            else:
                # path.append((x, y))
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_posn = (x, y-1)

        elif guard_dir == 'v':
        
            if x+1 > x_max - 1:
                escaped = True
                new_data[x][y] = 'X'
                break

            if new_data[x+1][y] == '#':
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_dir = '<'
                

            elif (len(new_data[x+1][y]) == 2 and 
                  guard_dir in new_data[x+1][y][1]):
                loop = True
                break
            
            else:
                # path.append((x, y))
                new_data[x][y] = ('X', {guard_dir}) if len (new_data[x][y]) == 1 else ('X', new_data[x][y][1] | {guard_dir})
                guard_posn = (x+1, y)

    return loop

loop_count = 0
for r in range(x_max):
    for c in range(y_max):
        if (r, c) == orig_guard_posn : continue
        print(r, c)
        loop_count += guard_loops(r, c)

print(loop_count)
