

def parse(lines):
    data = []
    for line in lines:
        p, v = line.split("@")
        px, py, pz = p.split(",")
        vx, vy, vz = v.split(",")

        data += [[int(px), int(py), int(pz), int(vx), int(vy), int(vz)]]
    return data

# given two lines, find the intersection point
# y = mx + c
# y = m1x + c1
# m1x + c1 = mx + c
# m1x - mx = c - c1
# x(m1 - m) = c - c1
# x = (c - c1) / (m1 - m)
# y = m1x + c1

def find_intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y4 - y3) / (x4 - x3)

    c1 = y1 - m1 * x1
    c2 = y3 - m2 * x3

    if (m1 - m2) == 0:
        return None, None

    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1

    return x, y

def solution(data, low, high):
    lines = []
    parallel = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1, z1, vx1, vy1, vz1 = data[i]
            x2, y2, z2, vx2, vy2, vz2 = data[j]
            px1, py1 = x1 + vx1, y1 + vy1
            px2, py2 = x2 + vx2, y2 + vy2

            x, y = find_intersection((x1, y1, px1, py1), (x2, y2, px2, py2))
            if x is None and y is None:
                parallel += [[data[i], data[j]]]
            if x is not None and y is not None:
                if x >= low and x <= high and y >= low and y <= high:
                    if (vx1 > 0 and x < x1) or (vx1 < 0 and x > x1):
                        continue
                    if (vx2 > 0 and x < x2) or (vx2 < 0 and x > x2):
                        continue
                    lines += [[x, y]]

    # for part 2, take the points at t1 and t2 for each permutation. These will give us a set of lines to test for intersection
    lines_to_test = []
    print(parallel)
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j: continue

            x1, y1, z1, vx1, vy1, vz1 = data[i]
            x2, y2, z2, vx2, vy2, vz2 = data[j]

            t1_x1, t1_y1, t1_z1 = x1 + vx1, y1 + vy1, z1 + vz1
            t2_x2, t2_y2, t2_z2 = x2 + vx2 * 2, y2 + vy2 * 2, z2 + vz2 * 2

            # our 3d velocity vector
            dx1, dy1, dz1 = t2_x2 - t1_x1, t2_y2 - t1_y1, t2_z2 - t1_z1

            # our 3d position vector at time 0
            x0, y0, z0 = x1 - dx1, y1 - dy1, z1 - dz1
            lines_to_test += [[x0, y0, z0, dx1, dy1, dz1]]


    #print(lines_to_test)
    # x0 + dx1 * t = x1 + dx2 * t
    # y0 + dy1 * t = y1 + dy2 * t
    # z0 + dz1 * t = z1 + dz2 * t
    # x0 - x1 = dx2 * t - dx1 * t
    # y0 - y1 = dy2 * t - dy1 * t
    # z0 - z1 = dz2 * t - dz1 * t
    # x0 - x1 = (dx2 - dx1) * t
    # y0 - y1 = (dy2 - dy1) * t
    # z0 - z1 = (dz2 - dz1) * t
    # t = (x0 - x1) / (dx2 - dx1)
    # t = (y0 - y1) / (dy2 - dy1)
    # t = (z0 - z1) / (dz2 - dz1)

    for x0, y0, z0, dx1, dy1, dz1 in lines_to_test:
        breakflag = False
        for x1, y1, z1, vx1, vy1, vz1 in data:
            if x0 == x1 or y0 == y1 or z0 == z1: continue
            if vx1 == dx1 or vy1 == dy1 or vz1 == dz1: continue

            t1 = (x0 - x1) / (dx1 - vx1)
            t2 = (y0 - y1) / (dy1 - vy1)
            t3 = (z0 - z1) / (dz1 - vz1)

            if t1 == t2 and t2 == t3:
                continue
            else:
                breakflag = True
                break

        if not breakflag:
            return x0, y0, z0
    return -1, -1, -1


if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day24/sample1.txt", "r")]
    parsed = parse(data)
    print(solution(parsed, 7, 27))

    # data_real = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day24/input1.txt", "r")]
    # parsed_real = parse(data_real)
    # print(solution(parsed_real, 200000000000000, 400000000000000))