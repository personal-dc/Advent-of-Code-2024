data = open('data/12-2.txt', 'r').read().split('\n')

int_data = []

for row in data:
    int_data.append([int(num) for num in row.split()])

## part 1 ##
safe_count = 0
for row in int_data:
    safe = True
    if row[0] < row[1]:
        for i in range(len(row)-1):
            if not (row[i]+1 <= row[i+1] <= row[i]+3):
                safe = False
                break

    else:
        for i in range(len(row)-1):
            if not (row[i]-1 >= row[i+1] >= row[i]-3):
                safe = False
                break

    safe_count += safe

print(safe_count)

## part 2 ##
def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in int_data])
print(safe_count)