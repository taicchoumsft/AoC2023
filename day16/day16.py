dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # E, S, W, N

def solution(data, initpos = (0, 0, 0)):
    dim_i, dim_j = len(data), len(data[0])
    q = [(initpos)] # i, j, dir
    seen = set()

    while q:
        i, j, dir = q.pop(0)
        if i < 0 or i >= dim_i or j < 0 or j >= dim_j: continue
        if (i, j, dir) in seen: continue
        seen.add((i, j, dir))

        match (data[i][j], dir):
            case ('.', _) | ('|', 1) | ('|', 3) | ('-', 0) | ('-', 2):
                new_i, new_j = i + dirs[dir][0], j + dirs[dir][1]
                q += [(new_i, new_j, dir)]
            case ('|', _):
                north_i, north_j = i + dirs[3][0], j + dirs[3][1]
                q += [(north_i, north_j, 3)]
                south_i, south_j = i + dirs[1][0], j + dirs[1][1]
                q += [(south_i, south_j, 1)]
            case ('-', _):
                east_i, east_j = i + dirs[0][0], j + dirs[0][1]
                q += [(east_i, east_j, 0)]
                west_i, west_j = i + dirs[2][0], j + dirs[2][1]
                q += [(west_i, west_j, 2)]
            case ('\\', _):
                dir = (dir + 1 if dir % 2 == 0 else dir - 1) % 4 # 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
                new_i, new_j = i + dirs[dir][0], j + dirs[dir][1]
                q += [(new_i, new_j, dir)]
            case ('/', _):
                dir = (dir - 1 if dir % 2 == 0 else dir + 1) % 4 # 0 -> 3, 1 -> 2, 2 -> 1, 3 -> 0
                new_i, new_j = i + dirs[dir][0], j + dirs[dir][1]
                q += [(new_i, new_j, dir)]

    test = [['.' for _ in range(dim_j)] for _ in range(dim_i)]

    total = 0
    for i, j, _ in seen:
        if test[i][j] != '#':
            test[i][j] = '#'
            total += 1

    return total

def solution2(data):
    dim_i, dim_j = len(data), len(data[0])
    best = 0
    for j in range(dim_j):
        best = max(best, solution(data, (0, j, 1))) # start top row, travel south
        best = max(best, solution(data, (dim_i - 1, j, 3))) # start bottom row, travel north

    for i in range(dim_i):
        best = max(best, solution(data, (i, 0, 0))) # start left col, travel east
        best = max(best, solution(data, (i, dim_j - 1, 2))) # start right col, travel west
    return best

if __name__ == "__main__":
    data = [line.strip() for line in open("./input1.txt", "r")]
    print(solution(data))
    print(solution2(data))
