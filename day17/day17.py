import heapq

dirs = [(0, 1, 0), (1, 0, 1), (0, -1, 2), (-1, 0, 3)] # east, south, west, north

def allowed_dirs(dir):
    if dir == 0 or dir == 2: # if east, west
        return [1, 3]
    elif dir == 1 or dir == 3:
        return [0, 2]# east, south, west

def solution(data):
    # try standard BFS
    dim_i, dim_j = len(data), len(data[0])
    q = [(0, 0, 0, 0, 0)] # cost, i, j, dir, counter after counter hits 3 we MUST turn
    seen = set()

    while q:
        cost, i, j, dir, counter = heapq.heappop(q)

        if i == dim_i - 1 and j == dim_j - 1:
            return cost

        if (i, j, dir, counter) in seen:
            continue
        seen.add((i, j, dir, counter))

        for new_dir in [*allowed_dirs(dir), dir]:
            new_i, new_j = i + dirs[new_dir][0], j + dirs[new_dir][1]
            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j:

                new_counter = counter + 1 if new_dir == dir else 1
                if new_counter <= 3:
                    heapq.heappush(q, (cost + int(data[new_i][new_j]), new_i, new_j, new_dir, new_counter))
    return -1

def canGoSteps(data, i, j, dir, steps):
    dim_i, dim_j = len(data), len(data[0])
    for _ in range(steps):
        i, j = i + dirs[dir][0], j + dirs[dir][1]
        if i < 0 or i >= dim_i or j < 0 or j >= dim_j:
            return False
    return True

def solution2(data):
    # now we have to use a heap
    dim_i, dim_j = len(data), len(data[0])
    q = [(0, 0, 0, 0, 0)] # cost, i, j, dir, counter must be at least 4, and max 10
    seen = set()

    while q:
        cost, i, j, dir, counter = heapq.heappop(q)

        if i == dim_i - 1 and j == dim_j - 1:
            return cost

        if (i, j, dir, counter) in seen:
            continue
        seen.add((i, j, dir, counter))

        if counter < 10:
            # continue going straight
            new_i, new_j = i + dirs[dir][0], j + dirs[dir][1]
            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j:
                #q += [(cost + int(data[new_i][new_j]), new_i, new_j, dir, counter + 1)]
                heapq.heappush(q, (cost + int(data[new_i][new_j]), new_i, new_j, dir, counter + 1))

        for new_dir in allowed_dirs(dir):
            if canGoSteps(data, i, j, new_dir, 4):
                new_i, new_j = i, j
                new_cost = 0
                for _ in range(4):
                    new_i, new_j = new_i + dirs[new_dir][0], new_j + dirs[new_dir][1]
                    new_cost += int(data[new_i][new_j])
                #q += [(cost + new_cost, new_i, new_j, new_dir, 4)]
                heapq.heappush(q, (cost + new_cost, new_i, new_j, new_dir, 4))

    return -1

# still can't get djikstra variant to work - why?
#
def solution_djikstra(data):
    dim_i, dim_j = len(data), len(data[0])
    dp = [[(float('inf'), 4) for _ in range(dim_j)] for _ in range(dim_i)]
    parents = [[None for _ in range(dim_j)] for _ in range(dim_i)]
    dp[0][0] = (0, 0)

    q = [(0, 0, 0, 0, 0)] # cost, counter, dir, i, j after counter hits 3 we MUST turn

    while q:
        cost, counter, dir, i, j = heapq.heappop(q)
        counter *= -1

        if i == dim_i - 1 and j == dim_j - 1:
            # grid = [["." for _ in range(dim_j)] for _ in range(dim_i)]
            # while parents[i][j]:
            #     arrow = '>' if parents[i][j][2] == 0 else '<' if parents[i][j][2] == 2 else 'v' if parents[i][j][2] == 1 else '^'
            #     grid[i][j] = arrow
            #     i, j, dir = parents[i][j]

            # for row in grid:
            #     print(''.join(row))
            return cost

        if counter < 3:
            # continue going straight
            new_i, new_j = i + dirs[dir][0], j + dirs[dir][1]
            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j and \
                cost + int(data[new_i][new_j]) < dp[new_i][new_j][0] and \
                counter + 1 < dp[new_i][new_j][1]:
                dp[new_i][new_j] = (cost + int(data[new_i][new_j]), counter + 1)
                parents[new_i][new_j] = (i, j, dir)
                heapq.heappush(q, (dp[new_i][new_j][0], -(counter + 1), dir, new_i, new_j))

        for new_dir in allowed_dirs(dir):
            new_i, new_j = i + dirs[new_dir][0], j + dirs[new_dir][1]
            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j and \
                cost + int(data[new_i][new_j]) < dp[new_i][new_j][0]:
                dp[new_i][new_j] = (cost + int(data[new_i][new_j]), 1)
                parents[new_i][new_j] = (i, j, new_dir)
                heapq.heappush(q, (dp[new_i][new_j][0], -1, new_dir, new_i, new_j))
    return -1

if __name__ == "__main__":
    data = [list(line.strip()) for line in open("./sample1.txt", "r")]
    print(solution(data)) # 1238
    print(solution_djikstra(data))
    print(solution2(data)) #1362

