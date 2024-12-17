
def mirror_horizontal(grid, allowed):
    for i in range(len(grid) - 1):
        cur = i
        j = i + 1
        allowed_count = allowed
        break_flag = False
        while i >= 0 and j < len(grid):
            if grid[i] != grid[j]:
                if sum(1 for a, b in zip(grid[i], grid[j]) if a != b) == 1 and allowed_count > 0:
                    allowed_count -= 1
                else:
                    break_flag = True
                    break
            i -= 1
            j += 1

        if not break_flag and allowed_count == 0:
            return cur + 1
    return -1

def solution(data, allowed = 0):
    grids = []

    grid = []
    for line in data:
        if line == "":
            grids += [grid]
            grid = []
            continue
        grid += [line]
    grids += [grid]

    total = 0
    for grid in grids:
        horiz = mirror_horizontal(grid, allowed)
        if horiz != -1:
            total += 100 * horiz
        else:
            # rotate by 90 degrees counter-clockwise
            # 1 2 3 4 5
            # 6 7 8 9 10

            # becomes
            # 5 10
            # 4 9 etc.
            grid = list(zip(*grid[::-1]))
            vertical = mirror_horizontal(grid, allowed)
            if vertical > -1:
                total += vertical

    return total

if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day13/input1.txt", "r")]
    print(solution(data))
    print(solution(data, 1))


#36822 wrong