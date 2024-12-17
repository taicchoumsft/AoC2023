from collections import defaultdict

def solution(grid, goal = 64):
    dim_i, dim_j = len(grid), len(grid[0])

    for i in range(dim_i):
        for j in range(dim_j):
            if grid[i][j] == "S":
                start_i, start_j = i, j
                grid[i][j] = "."
                break

    q = [(start_i, start_j)]

    steps = 0
    while q:
        sz = len(q)
        while sz > 0:
            i, j = q.pop(0)

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                if 0 <= i + di < dim_i and 0 <= j + dj < dim_j and grid[i + di][j + dj] == ".":
                    q.append((i + di, j + dj))

            sz -= 1
        q = list(set(q))

        steps += 1
        if steps == goal:
            break

    return len(q)

def solution2(grid, goal = 26501365):
    dim_i, dim_j = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(dim_i):
        for j in range(dim_j):
            if grid[i][j] == "S":
                start_i, start_j = i, j
                grid[i][j] = "."
                break

    q = [(start_i, start_j)]

    steps = 0
    seen = set()

    a = []

    while q:
        sz = len(q)
        seen.clear()

        while sz > 0:
            i, j = q.pop(0)

            for di, dj in dirs:
                new_i, new_j = i + di, j + dj

                if grid[new_i % dim_i][new_j % dim_j] == "." and (new_i, new_j) not in seen:
                    q += [(new_i, new_j)]
                    seen.add((new_i, new_j))
            sz -= 1

        steps += 1
        if steps % dim_i == goal % dim_i:
            print(steps, len(q))
            a += [len(q)]
        if len(a) == 3:
            break
    return a


# research: https://en.wikipedia.org/wiki/Newton_polynomial
def f(a, n):
    b0 = a[0]
    b1 = a[1]-a[0]
    b2 = a[2]-a[1]
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

if __name__ == "__main__":
    data = [list(line.strip()) for line in open("/Users/chou/source/workspace/aoc2023/day21/input1.txt", "r")]
    print(solution(data))
    goal = 26501365
    data = [list(line.strip()) for line in open("/Users/chou/source/workspace/aoc2023/day21/input1.txt", "r")]
    a = solution2(data, goal)
    print(f(a, goal//len(data)))

