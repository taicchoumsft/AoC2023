import bisect


def solution(grid):
    def expand(data):
        row_idxes = []
        col_idxes = []
        for row_idx, row in enumerate(data):
            if all([x == "." for x in row]):
                row_idxes += [row_idx]

        for j in range(len(data[0])):
            if all([data[i][j] == "." for i in range(len(data))]):
                col_idxes += [j]
        return row_idxes, col_idxes
        # new_data = []
        # for idx, row in enumerate(data):
        #     new_data += [row]
        #     if idx in row_idxes: new_data += [row]

        # new_data2 = [[] for _ in range(len(new_data))]
        # for col_idx in range(len(new_data[0])):
        #     for row_idx in range(len(new_data)):
        #         new_data2[row_idx] += [new_data[row_idx][col_idx]]

        #         if col_idx in col_idxes:
        #             new_data2[row_idx] += ["."]

        # return new_data2

    row_idxes, col_idxes = expand(grid)
    for row in grid:
        print("".join(row))

    # store all the coords of the universes
    points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                points += [(i, j)]

    # calculate manhattan dist between all points
    total = 0
    manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    factor = 1000000 - 1
    for m in range(len(points)):
        for n in range(m + 1, len(points)):
            mn, mx = min(points[m][0], points[n][0]), max(points[m][0], points[n][0])
            i1 = bisect.bisect_left(row_idxes, mn)
            i2 = bisect.bisect_left(row_idxes, mx)

            mn, mx = min(points[m][1], points[n][1]), max(points[m][1], points[n][1])
            j1 = bisect.bisect_left(col_idxes, mn)
            j2 = bisect.bisect_left(col_idxes, mx)
            to_add_i = (i2 - i1) * factor
            to_add_j = (j2 - j1) * factor
            print(points[m], points[n], to_add_i, to_add_j, manhattan(points[m], points[n]))
            total += manhattan(points[m], points[n]) + to_add_i + to_add_j
    return total

if __name__ == "__main__":
    data = [list(line.strip()) for line in open("input1.txt", "r")]
    print(solution(data))

# 692507033160 wrong

