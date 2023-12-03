def find_connection(data, row, col):
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(data) and 0 <= j < len(data[i]) and not data[i][j].isdigit() and data[i][j] != '.':
                if data[i][j] == '*': # part 2
                    return (True, i, j)
                return (True, -1,-1)
    return (False, -1,-1)

def solve(data):
    p1 = 0
    p2 = 0
    stars = {}
    for row in range(len(data)):
        connected, i, j = False, -1, -1
        num = ''
        for col in range(len(data[row])):
            if data[row][col].isdigit():
                if not connected:
                    connected, i, j = find_connection(data, row, col)
                elif i == -1 and j == -1:
                    _, i, j = find_connection(data, row, col)
                num += data[row][col]
            if not data[row][col].isdigit() or col == len(data[row]) - 1:
                if connected:
                    p1 += int(num)
                    if (i,j) in stars:
                        p2 += int(stars[(i,j)]) * int(num)
                    elif i != -1 and j != -1:
                        stars[(i,j)] = num
                    connected = False
                num = ''
    return p1, p2

if __name__ == '__main__':
    data = open("input.txt").read().split("\n")
    res = 0
    p1, p2 = solve(data)

    print("Part 1: ", p1)
    print("Part 2: ", p2)