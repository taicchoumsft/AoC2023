from collections import defaultdict
import copy

def parse(data):
    results = []
    for line in data:
        a, b = line.split("~")
        x1,y1,z1 = a.split(",")
        x2,y2,z2 = b.split(",")
        x1,y1,z1 = int(x1), int(y1), int(z1)
        x2,y2,z2 = int(x2), int(y2), int(z2)
        results += [[[x1,y1,z1], [x2,y2,z2]]]
        assert x1 <= x2 and y1 <= y2 and z1 <= z2
    return results

# bird eye view
def testForOverlap(bricks, cur_brick):
    s1_start, s1_stop = cur_brick
    overlaps = []
    res = False
    for s2_start, s2_stop in bricks:
        if  max(s1_start[0], s2_start[0]) <= min(s1_stop[0], s2_stop[0]) and \
            max(s1_start[1], s2_start[1]) <= min(s1_stop[1], s2_stop[1]) and \
            max(s1_start[2], s2_start[2]) <= min(s1_stop[2], s2_stop[2]):
            overlaps += [[s2_start, s2_stop]]
            res = True
    return res, overlaps

def dropBrick(bricks, cur_brick, supports):
    didOverlap, overlaps = False, None
    while not didOverlap and cur_brick[0][2] > 0:
        cur_brick[0][2] -= 1
        cur_brick[1][2] -= 1
        didOverlap, overlaps = testForOverlap(bricks, cur_brick)

    cur_brick[0][2] += 1
    cur_brick[1][2] += 1

    for overlap in overlaps:
        supports[tuple(overlap[0]), tuple(overlap[1])].add((tuple(cur_brick[0]), tuple(cur_brick[1])))

    bricks += [cur_brick]
    #bricks.sort(key=lambda x: x[0][2])

def solution(arr):
    arr.sort(key=lambda x: (x[0][2], x[1][2]))
    supports = defaultdict(set)

    compressed = []
    for brick1 in arr:
        dropBrick(compressed, brick1, supports)

    dependent_on = defaultdict(set)

    arr = compressed
    count = 0

    for k, vs in supports.items():
        for v in vs:
            dependent_on[v].add(k)

    for brick1 in arr:
        start_1, stop_1 = brick1
        for start_2, stop_2 in supports[tuple(start_1), tuple(stop_1)]:
            assert(len(dependent_on[(tuple(start_2), tuple(stop_2))]) > 0)
            if len(dependent_on[(tuple(start_2), tuple(stop_2))]) <= 1:
                count += 1
                break

    def dfs(brick, seen):
        if brick in seen:
            return
        seen.add(brick)

        for b in supports[tuple(brick[0]), tuple(brick[1])]:
            remaining = dependent_on[b] - seen
            if len(remaining) == 0:
                dfs(b, seen)

    count2 = 0
    for brick in arr:
        seen = set()
        dfs((tuple(brick[0]), tuple(brick[1])), seen)
        count2 += len(seen) - 1

    return len(arr) - count, count2

if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day22/input1.txt", "r")]

    print(solution(parse(data)))


# 134282 too high
    # 66743 too high