from collections import defaultdict


def solve(data, p1, p2):
    card_count = defaultdict(lambda: 1)
    for i, (win, own) in enumerate(data):
        win = set(list(map(int, win.split())))
        own = set(list(map(int, own.split())))
        card_number = i+1
        same = len(win.intersection(own))

        if len(win.intersection(own)) > 0:
            p1 += 2 ** (same-1)
            for e in range(card_number + 1, card_number + 1 + same):
                card_count[e] += card_count[card_number]
        p2 += card_count[card_number]
    return p1, p2


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    data = [x.split(": ")[1].split(' | ') for x in data]
    p1, p2 = solve(data, 0, 0)
    print("Part 1:", p1)
    print("Part 2:", p2)