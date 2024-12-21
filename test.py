import itertools


x = [0, 1, 2, 3, 4, 5, 6]

free = 2
l = len(x)

cut = x[l -free : ]
new = x[: l - free]

print(new, cut)