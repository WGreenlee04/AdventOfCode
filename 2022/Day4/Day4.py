answer = 0


for line in open("C:/Users/Green/git/AdventOfCode/2022/Day4/input.txt"):
    line = line.strip()
    ranges = line.split(",")
    temp = ranges[0].split("-")
    s1 = set(range(int(temp[0]), int(temp[1])+1))
    temp = ranges[1].split("-")
    r2 = set(range(int(temp[0]), int(temp[1])+1))

    inter: set = s1.intersection(r2)
    if (len(inter) > 0):
        answer += 1

print(answer)
