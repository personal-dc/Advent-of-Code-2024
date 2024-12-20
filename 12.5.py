from collections import defaultdict

data = open('data/12-5.txt', 'r').read().split('\n\n')

rules, orderings = [d.split('\n') for d in data]

## part 1 ##
graph = defaultdict(lambda : set())

for r in rules:
    frm, to = [int(x) for x in r.split('|')]
    graph[to] = graph[to] | {frm}

path_list = []

for o in orderings:
    if o : path_list.append([int(x) for x in o.split(',')])

corr_paths = []
for path in path_list:
    corr = True
    for i in range(len(path)):
        right_set = set(path[i+1:])
        
        if (right_set.intersection(graph[path[i]]) != set()) : 
            corr = False
            break
    
    if corr : corr_paths.append(path)

sum = 0
for path in corr_paths:
    assert len(path) % 2 == 1
    sum += path[int(len(path)/2)]

print(sum)

## part 2 ##
def filter_graph(graph, nodes):
    return {node : graph[node].intersection(nodes) for node in nodes}

path_list = []

for o in orderings:
    if o : path_list.append([int(x) for x in o.split(',')])

incorr_paths = []
for path in path_list:
    corr = True
    for i in range(len(path)):
        right_set = set(path[i+1:])
        
        if (right_set.intersection(graph[path[i]]) != set()) : 
            corr = False
            break
    
    if not corr : incorr_paths.append(path)

updated_paths = []
for path in incorr_paths:
    path_set = set(path)
    filtered_graph = filter_graph(graph, path_set)
    path_len = len(path_set)
    new_path = []
    while len(new_path) < path_len:
        for node in filtered_graph.keys():
            if filtered_graph[node] == set():
                new_path.append(node)
                path_set = path_set - {node}
                filtered_graph = filter_graph(filtered_graph, path_set)
                break

    updated_paths.append(new_path)

sum = 0
for path in updated_paths:
    assert len(path) % 2 == 1
    sum += path[int(len(path)/2)]

print(sum)