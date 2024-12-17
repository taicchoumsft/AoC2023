
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # E, S, W, N

def parse(line):
    dir, ln, color = line.split(" ")
    color = color[1:-1]
    return dir, int(ln), color

def getPoints(parsed_data, use_color = False):
    # Surveyer's formula - but have to adjust for concave corners
    i, j = 0, 0
    points = [(i, j)]

    # ultimately, we are given a border that we have to stay within, but the border
    # has thickness 1, so we have to extend the border by 1
    # but we also have to reduce the length by 1 whenever we have a concave corner
    # because of the thickness of the border
    # we can always treat the problem as going clockwise
    for idx, line in enumerate(parsed_data):
        dir, ln, color = line
        if use_color:
            ln = int(color[1:-1], 16)
            dir = ["R", "D", "L", "U"][int(color[-1])]

        ln += 1
        match dir:
            case "U":
                if parsed_data[(idx + 1) % len(parsed_data)][0] == "L": ln -= 1
                if parsed_data[(idx - 1)][0] == "R": ln -= 1
                i -= ln
            case "D":
                if parsed_data[(idx + 1) % len(parsed_data)][0] == "R": ln -= 1
                if parsed_data[(idx - 1)][0] == "L": ln -= 1
                i += ln
            case "L":
                if parsed_data[(idx + 1) % len(parsed_data)][0] == "D": ln -= 1
                if parsed_data[(idx - 1)][0] == "U": ln -= 1
                j -= ln
            case "R":
                if parsed_data[(idx + 1) % len(parsed_data)][0] == "U": ln -= 1
                if parsed_data[(idx - 1)][0] == "D": ln -= 1
                j += ln
        points += [(i, j)]

    points += [(0, 0)]
    return points

# shoelace formula, surveryor's formula etc. - https://en.wikipedia.org/wiki/Shoelace_formula
def area(points):
    area = 0
    for (i1, j1), (i2, j2) in zip(points[:-1], points[1:]):
        area += (i1 * j2 - i2 * j1)
    return abs(area) // 2

def solution(parsed_data, use_color = False):
    points = getPoints(parsed_data, use_color)
    return area(points)

if __name__ == "__main__":
    data = [line.strip() for line in open("./input1.txt", "r")]
    parsed_data = [parse(line) for line in data]

    print(solution(parsed_data)) # 58850 is correct
    print(solution(parsed_data, use_color=True))

