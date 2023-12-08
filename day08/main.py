from math import lcm




def steps_to_z(node, dict, rl):
    s = 0
    while True:
        for c in rl:
            node = dict[node][c == "R"]
            s += 1
            if node.endswith("Z"):
                return s


def part2(dict, rl):
    starts = []
    for x in dict:
        if x[2] == 'A':
            starts.append(x)
    return lcm(*[steps_to_z(_a, dict, rl) for _a in dict if _a.endswith("A")])


def part1(dict, rl):
    return steps_to_z('AAA',dict, rl)


def parseData(data):
    rl = data[0]
    data = data[2:]
    data = [i.split(" = ") for i in data]
    data = [[i[0], tuple(i[1][1:-1].split(', '))] for i in data]

    dict = {}
    for x, t in data:
        dict[x] = t
    return rl, dict

if __name__ == '__main__':
    rl, dict = parseData(open("input.txt").read().split("\n"))

    print("Part 1:", part1(dict, rl))
    print("Part 2:", part2(dict, rl))