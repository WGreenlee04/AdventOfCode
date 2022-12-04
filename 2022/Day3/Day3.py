from itertools import islice
import string

with open("C:/Users/Green/git/AdventOfCode/2022/Day3/input.txt") as f:
    ls = [x.strip() for x in f.readlines()]

score = (" " + string.ascii_lowercase + string.ascii_uppercase).index


sets = map(set, ls)
s = 0
for _ in range(len(ls) // 3):
    (o,) = set.intersection(*islice(sets, 3))
    s += score(o)
print(s)

