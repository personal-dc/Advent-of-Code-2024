import itertools
from collections import deque

data = open('data/12-7.txt', 'r').read().strip().split('\n')

sol_num_pairs = [d.split(':') for d in data]
sol_num_pairs = [(int(d[0]), [int(n) for n in d[1].split(' ')[1:]]) for d in sol_num_pairs]

## part 1 ##

solvable = []
for sol, nums in sol_num_pairs:
    l = len(nums) - 1
    bin_combs = [list(i) for i in itertools.product([0, 1], repeat=l)]
    
    
    for comb in bin_combs:
        num_deque = deque(nums)
        op_funcs = deque(map(lambda c : (lambda x, y : x*y) if c else (lambda x, y : x+y), comb))
        calc = num_deque.popleft()
        while num_deque:
            func = op_funcs.popleft()
            calc = func(calc, num_deque.popleft())
        
        if calc == sol : 
            solvable.append(sol)
            break

print(sum(solvable))

## part 2 ##

def get_func(op):
    match op:
        case 0:
            return lambda x, y : x+y

        case 1:
            return lambda x, y : x*y

        case 2:
            return lambda x, y : int(str(x)+str(y))


solvable = []

for sol, nums in sol_num_pairs:
    l = len(nums) - 1
    bin_combs = [list(i) for i in itertools.product([0, 1, 2], repeat=l)]
    
    
    for comb in bin_combs:
        num_deque = deque(nums)
        op_funcs = deque(map(lambda c : get_func(c), comb))
        calc = num_deque.popleft()
        while num_deque:
            func = op_funcs.popleft()
            calc = func(calc, num_deque.popleft())
        
        if calc == sol : 
            solvable.append(sol)
            break

print(sum(solvable))