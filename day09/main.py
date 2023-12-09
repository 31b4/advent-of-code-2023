data = open("input.txt").read().split("\n")
data = [list(map(int, i.split())) for i in data]

def solve(l):
	if set(l) == {0}:
		return 0

	next = []
	for i in range(len(l)-1):
		next.append(l[i+1]-l[i])

	return l[-1] + solve(next)

print("Part 1:", sum(solve(l) for l in data))
print("Part 2:", sum(solve(l[::-1]) for l in data))