def Solve(blocks):
    maxColorsInBlocks = {"red": 0, "green": 0, "blue": 0}

    for block in blocks:
        e = block.split(", ")
        for sv in e:
            amount = int(sv.split(" ")[0])
            color = sv.split(" ")[1]
            maxColorsInBlocks[color] = max(maxColorsInBlocks[color], amount)

    return maxColorsInBlocks


if __name__ == '__main__':
    lines = open("input.txt").read().strip().split("\n")
    maxes = {"red": 12, "green": 13, "blue": 14}
    p1 = 0
    p2 = 0

    for game_id, line in enumerate(lines):
        line = line.split(": ")[1]
        blocks = line.split("; ")
        maxColorsInBlocks = Solve(blocks)

        for color in maxes:
            if maxColorsInBlocks[color] > maxes[color]:
                break
        else:
            p1 += game_id + 1
        p2 += maxColorsInBlocks["red"] * maxColorsInBlocks["green"] * maxColorsInBlocks["blue"]

    print("Part 1:", p1)
    print("Part 2:", p2)