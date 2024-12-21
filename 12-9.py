data = [int(n) for n in list(open('data/12-9.txt', 'r').read().strip())]

## part 1 ## 

blanks = []

disk_map = {}
disk_id = 0
last_id = None
for ind, num in enumerate(data):
    if ind%2 == 0:
        id = int(ind/2)
        for i in range(num):
            disk_map[disk_id+i] = id
            last_id = disk_id+i
        
        disk_id += num

    else:
        for i in range(num):
            disk_map[disk_id+i] = None
            blanks.append(disk_id+i)
        
        disk_id += num


while blanks and last_id >= blanks[0]:
    while disk_map[last_id] is None : last_id -=1
    if last_id < blanks[0] : break
    disk_map[blanks[0]] = disk_map[last_id]
    disk_map[last_id] = None
    blanks.pop(0)
    last_id -=1

sum = 0
for id, num in disk_map.items():
    num = num if num is not None else 0
    sum += (id*num)

print(sum)

## part 2 ##
# data = '2333133121414131402'
# data = [int(d) for d in list(data)]
blanks = []
files_map = {}
files_id_map = {}

disk_map = {}
disk_id = 0
last_id = None
for ind, num in enumerate(data):
    if ind%2 == 0:
        id = int(ind/2)
        files_map[id] = num
        files_id_map[id] = [i for i in range(disk_id, disk_id+num)]
        for i in range(num):
            disk_map[disk_id+i] = id
            last_id = id
        
        disk_id += num

    else:
        for i in range(num):
            disk_map[disk_id+i] = None
        blanks.append((disk_id, disk_id+num-1))
        disk_id += num

while last_id >= 0:
    id_space = files_map[last_id]

    free_id = 0
    while free_id < len(blanks):
        start, end = blanks[free_id]
        if start > files_id_map[last_id][0] : break
        if end-start+1 >= id_space :
            for i in range(start, start+id_space):
                disk_map[i] = last_id
            
            for i in files_id_map[last_id]:
                disk_map[i] = None

            blanks[free_id] = (start+id_space, end)
            break

        else : free_id+=1

    last_id -= 1 

# print(disk_map.values())
sum = 0
for id, num in disk_map.items():
    num = num if num is not None else 0
    sum += (id*num)

print(sum)