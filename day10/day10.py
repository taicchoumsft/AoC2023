import sys
sys.setrecursionlimit(100000)

dirs = [(0, 1, set(["-", "7", "J"])), (1, 0, set(["|", "L", "J"])), (-1, 0, set(["|", "F", "7"])), (0, -1, set(["-", "L", "F"]))]

def solution(grid):
    dim_i, dim_j = len(grid), len(grid[0])

    for i in range(dim_i):
        for j in range(dim_j):
            if grid[i][j] == "S":
                sp = (i, j)
                break

    def backtrack(i, j, cur, best):
        for dir_i, dir_j, allowed in dirs:
            new_i, new_j = i + dir_i, j + dir_j

            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j:

                if (new_i, new_j) == sp and len(cur) > len(best[0]):
                    best[0] = cur.copy()

                if (new_i, new_j) not in cur and \
                    grid[new_i][new_j] in allowed:
                    cur.add((new_i, new_j))
                    backtrack(new_i, new_j, cur, best)
                    cur.remove((new_i, new_j))

    best = [set()]
    backtrack(sp[0], sp[1], set(), best)
    return best[0], sp

def solution2(grid, path, sp):
    # 1) Filter out everything but the hull
    # 2) Double the grid to see the gaps
    # 3) Flood fill the gaps from the edges
    # 4) Collapse the grid back to normal

    def flood_fill(grid, i, j, path):
        dim_i, dim_j = len(grid), len(grid[0])

        if grid[i][j] != '.': return
        grid[i][j] = "X"

        for dir_i, dir_j, _ in dirs:
            new_i, new_j = i + dir_i, j + dir_j
            if new_i >= 0 and new_i < dim_i and \
                new_j >= 0 and new_j < dim_j and \
                grid[new_i][new_j] == ".":
                flood_fill(grid, new_i, new_j, path)

    def expand_grid(grid):
        # expand each row, connect with "-" or "|" if possible
        grid2 = []
        for row in grid:
            newRow = [row[0]]
            for i1, i2 in zip(row[:-1], row[1:]):
                fill = "-" if i1 in {"F", "L", "-", "S"} and i2 in {"7", "J", "-", "S"} else "."
                newRow += [fill, i2]
            grid2 += [newRow]

        # expand the columns
        grid3 = [grid2[0]]
        for r1, r2 in zip(grid2[:-1], grid2[1:]):
            newRow = []
            for i1, i2 in zip(r1, r2):
                fill = "|" if (i1 in {"7","F", "S", "|"} and i2 in {"J", "L", "S", "|"}) else "."
                newRow += [fill]
            grid3 += [newRow, r2]
        return grid3

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in path and (i, j) != sp:
                grid[i][j] = "."

    grid = expand_grid(grid)

    # now flood fill all "."s from the edges
    for i in range(len(grid)):
        flood_fill(grid, i, 0, path)
        flood_fill(grid, i, len(grid[0]) - 1, path)

    for j in range(len(grid[0])):
        flood_fill(grid, 0, j, path)
        flood_fill(grid, len(grid) - 1, j, path)

    # collapse the columns back to original size
    newGrid = []
    for i in range(0, len(grid), 2):
        newRow = [grid[i][j] for j in range(0, len(grid[0]), 2)]
        newGrid += [newRow]

    # take the sum of all the "."s
    return sum(row.count(".") for row in newGrid)

if __name__ == "__main__":
    data = [list(line.strip()) for line in open("input1.txt", "r")]
    path, sp = solution(data)
    print("Solution 1: ", (len(path) + 1) // 2)
    print("Solution 2: ", solution2(data, path, sp))
