import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up

def solution(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    # backtracking
    def dfs(grid, i, j, dir, seen, steps, results):
        if i == dim_i - 1 and j == dim_j - 2:
            results += [steps]
            return

        for dir, (d_i, d_j) in enumerate(dirs):
            new_i, new_j = i + d_i, j + d_j
            if 0 <= new_i < dim_i and 0 <= new_j < dim_j and \
                (grid[new_i][new_j] == "." or \
                (grid[new_i][new_j] == ">" and dir == 0) or \
                (grid[new_i][new_j] == "<" and dir == 1) or \
                (grid[new_i][new_j] == "v" and dir == 2) or \
                (grid[new_i][new_j] == "^" and dir == 3)
                ) and \
                (new_i, new_j) not in seen:
                seen.add((new_i, new_j))
                dfs(grid, new_i, new_j, dir, seen, steps + 1, results)
                seen.remove((new_i, new_j))

    results = []
    dfs(grid, 0, 1, 2, set(), 0, results)
    return max(results)

def isIntersection(grid, i, j):
    if grid[i][j] == "#":
        return False

    dim_i, dim_j = len(grid), len(grid[0])

    count = 0
    for d_i, d_j in dirs:
        new_i, new_j = i + d_i, j + d_j
        if 0 <= new_i < dim_i and 0 <= new_j < dim_j and grid[new_i][new_j] != "#":
            count += 1

    return count > 2

def solution2(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    def build_maze(grid, i, j, steps, parent, last_intersection, adj_list):
        if (i, j) == (dim_i - 1, dim_j - 2) or (i, j) == (0, 1):
            adj_list[last_intersection].add((i, j, steps))
            adj_list[(i, j)].add((last_intersection[0], last_intersection[1], steps))
            return

        if isIntersection(grid, i, j) and (i, j) != last_intersection:
            adj_list[last_intersection].add((i, j, steps))
            adj_list[(i, j)].add((last_intersection[0], last_intersection[1], steps))
            return

        for d_i, d_j in dirs:
            new_i, new_j = i + d_i, j + d_j
            if 0 <= new_i < dim_i and 0 <= new_j < dim_j and \
                grid[new_i][new_j] != "#" and (new_i, new_j) != parent:
                build_maze(grid, new_i, new_j, steps + 1, (i, j), last_intersection, adj_list)

    # build an adj_list to prune the maze (i.e. just keep intersections)
    # then do the step 1 backtracking again
    adj_list = defaultdict(set)
    for i in range(dim_i):
        for j in range(dim_j):
            if isIntersection(grid, i, j):
                build_maze(grid, i, j, 0, (i, j), (i, j), adj_list)

    def dfs2(adj_list, seen, i, j, steps, results):
        if i == dim_i - 1 and j == dim_j - 2:
            results.add(steps)
            return

        for new_i, new_j, new_steps in adj_list[(i, j)]:
            if (new_i, new_j) not in seen:
                seen.add((new_i, new_j))
                dfs2(adj_list, seen, new_i, new_j, steps + new_steps, results)
                seen.remove((new_i, new_j))

    results = set()
    dfs2(adj_list, set(), 0, 1, 0, results)
    return max(results)

if __name__ == "__main__":
    grid = [line.strip() for line in open("./input1.txt", "r")]
    print(solution(grid))
    print(solution2(grid))
