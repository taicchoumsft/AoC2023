# go north is (-1 , 0) etc.
def simulate(grid, i, j, dir_i, dir_j):
    dim_i, dim_j = len(grid), len(grid[0])
    while 0 <= i + dir_i < dim_i and 0 <= j + dir_j < dim_j:
        if grid[i + dir_i][j + dir_j] != ".":
            return
        grid[i][j] = "."
        grid[i + dir_i][j + dir_j] = "O"
        i += dir_i
        j += dir_j

#simulate from top to bottom
def solution(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    for i in range(dim_i):
        for j in range(dim_j):
            if data[i][j] == "O":
                simulate(grid, i, j, -1, 0)

    total = 0
    for idx, row in enumerate(grid):
        total += (dim_i - idx) * sum(1 for c in row if c == "O")

    return total

def one_cycle(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    for i in range(dim_i):
        for j in range(dim_j):
            if data[i][j] == "O":
                simulate(grid, i, j, -1, 0)
    # west
    for i in range(dim_i):
        for j in range(dim_j):
            if data[i][j] == "O":
                simulate(grid, i, j, 0, -1)

    # south
    for i in range(dim_i - 1, -1, -1):
        for j in range(dim_j):
            if data[i][j] == "O":
                simulate(grid, i, j, 1, 0)

    # east
    for i in range(dim_i):
        for j in range(dim_j - 1, -1, -1):
            if data[i][j] == "O":
                simulate(grid, i, j, 0, 1)

    # print()
    # for row in grid:
    #     print("".join(row))

def hash(grid):
    return "@".join("+".join(row) for row in grid)

def solution2(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    cnt = 1
    mp = dict()
    cycle_len = 0
    while True:
        one_cycle(grid)
        h = hash(grid)
        if h in mp:
            print("Found cycle at: ", cnt, mp[h])
            cycle_len = cnt - mp[h]
            break
        mp[h] = cnt
        cnt += 1

    print("Cycle length: ", cycle_len)
    # cnt is starting point of cycle, we can jump forward and find the remaining steps by taking modulo
    target = (1000000000 - cnt) % cycle_len
    for _ in range(target):
        one_cycle(grid)

    return sum((dim_i - idx) * sum(1 for c in row if c == "O") for idx, row in enumerate(grid))

if __name__ == "__main__":
    data = [list(line.strip()) for line in open("/Users/chou/source/workspace/aoc2023/day14/input1.txt", "r")]
    print(solution(data))
    print(solution2(data))


