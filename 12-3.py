import re

data = open('data/12-3.txt', 'r')

## part 1 ##
get_muls = re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", data.read())

sum = 0
for mul in get_muls:
    x, y = re.findall('[0-9]{1,3}', mul)
    sum+= (int(x)*int(y))

# print(sum)

## part 2 ##

data = open('data/12-3.txt', 'r')
get_muls = re.findall("(mul[(][0-9]{1,3},[0-9]{1,3}[)])|(do[(][)])|(don't[(][)])", data.read())

get_muls = list(map(lambda x : x[0]+x[1]+x[2], get_muls))

print(get_muls)

sum = 0
disabled = False
for token in get_muls:
    if token == "don't()" :
        disabled = True
    elif token == "do()" :
        disabled = False
    else:
        if not disabled:
            x, y = re.findall('[0-9]{1,3}', token)
            sum+= (int(x)*int(y))

print(sum)
