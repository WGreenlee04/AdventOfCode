totals = []
index = [0]


def stuff(line, index, totals):
    if (line == "\n"):
        index[0] += 1
    else:
        if (index[0] >= len(totals)):
            totals.append(int(line))
        else:
            totals[index[0]] += int(line)


for line in open("C:/Users/Green/git/AdventOfCode/2022/Day1/input.txt"):
    stuff(line, index, totals)


totals = sorted(totals, reverse=True)

print(totals[0]+totals[1]+totals[2])
