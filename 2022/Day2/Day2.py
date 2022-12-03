total = 0


def convert(n: str):
    if (n == "A" or n == "Y\n"):
        return 0
    if (n == "B" or n == "Z\n"):
        return 1
    if (n == "C" or n == "X\n"):
        return 2


def iterate_convert(n):
    nc = n.copy()
    for i in range(0, len(nc)):
        nc[i] = convert(nc[i])
    return nc


def stuff(line: str):
    global total
    temprps = line.split(" ")
    rps: list(int) = iterate_convert(temprps)
    rps[1] = (rps[0]+rps[1]) % 3
    if (temprps[1] == "Z\n"):
        total += (6+(rps[1]+1))
    elif (temprps[1] == "Y\n"):
        total += (3+(rps[1]+1))
    else:
        total += int((rps[1]+1))


for line in open("C:/Users/Green/git/AdventOfCode/2022/Day2/input.txt"):
    stuff(line)

print(total)
