from collections import Counter

data = open("input.txt").read().split("\n")
data = [i.split() for i in data]
data = [[i[0], int(i[1])] for i in data]

def convert(hand):
    hand = list(hand)
    for i in range(len(hand)):
        if hand[i] == 'T':
            hand[i] = 10
        elif hand[i] == 'J':# joker worth 0 point
            hand[i] = 0
        elif hand[i] == 'Q':
            hand[i] = 12
        elif hand[i] == 'K':
            hand[i] = 13
        elif hand[i] == 'A':
            hand[i] = 14
        else:
            hand[i] = int(hand[i])
    return hand


five = []
four = []
full = []
three = []
two = []
one = []
high = []

for i, (cards, point) in enumerate(data):
    hand = convert(cards)
    cnt = Counter(hand)
    if 0 in cnt:
        sorted_by_common = cnt.most_common()
        if sorted_by_common[0][0] == 0:
            if len(sorted_by_common) != 1:
                most_common = sorted_by_common[1][0]
                cnt[most_common] += cnt[0]
                del cnt[0]
        else:
            most_common = sorted_by_common[0][0]
            cnt[most_common] += cnt[0]
            del cnt[0]

    if len(set(cnt)) == 1:  # Five of a kind
        five.append((hand, i))
    elif len(set(cnt)) == 5:  # High card
        high.append((hand, i))
    elif len(set(cnt)) == 2:  # four or full
        for c in cnt:
            if cnt[c] == 4:  # Four of a kind
                four.append((hand, i))
                break
            elif cnt[c] == 3:  # Full house
                full.append((hand, i))
                break
    elif len(set(cnt)) == 3:  # three or two
        for c in cnt:
            if cnt[c] == 3:  # Three of a kind
                three.append((hand, i))
                break
            elif cnt[c] == 2:  # Two pair
                two.append((hand, i))
                break
    elif len(set(cnt)) == 4:  # One pair
        one.append((hand, i))

five.sort()
four.sort()
full.sort()
three.sort()
two.sort()
one.sort()
high.sort()

res = 0
for i, x in enumerate(high+one+two+three+full+four+five):
    res += data[x[1]][1] * (i+1)

print("Part 2:",res)