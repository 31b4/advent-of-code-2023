from math import sqrt, floor, ceil
data = open("input.txt").read().split("\n")

# Part 1
times = list(map(int,data[0].split(": ")[1].split()))
dists = list(map(int,data[1].split(": ")[1].split()))
p1 = 1
for i, time in enumerate(times):
    sv = 0
    for ms in range(time):
        if ms * (time-ms) > dists[i]:
            sv += 1
    p1 *= sv
print("Part 1:", p1)

# Part 2
time = int("".join(data[0].split(": ")[1].split()))
dist = int("".join(data[1].split(": ")[1].split()))

gyok1 = (time + sqrt(time ** 2 - 4 * dist)) / 2
gyok2 = (time - sqrt(time ** 2 - 4 * dist)) / 2
print("Part 2:", floor(gyok1) - ceil(gyok2)+1)


