import re
import copy

def parse(data):
    workflows = dict()
    items = []

    for line in data:
        if line == "":
            break

        delim = line.index("{")
        key = line[:delim].strip()
        values = line[delim + 1:-1].split(",")

        value_lst = [(cond, to) for cond, to in [value.split(":") for value in values[:-1]]]
        workflows[key] = value_lst + [(None, values[-1])]


    for line in data:
        m = re.match("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line)
        if m:
            x, m, a, s = m.groups()
            items += [{"x": int(x), "m": int(m), "a":int(a), "s":int(s)}]

    return workflows, items

def test(workflows, item, workflow="in"):
    if workflow == "R":
        return False
    elif workflow == "A":
        return True

    # these are being eval'd
    x = item["x"]
    m = item["m"]
    a = item["a"]
    s = item["s"]

    for cond, to in workflows[workflow]:
        if not cond or eval(cond):
            return test(workflows, item, to)

    return False

def solution(workflows, items):
    total = 0
    for item in items:
        if test(workflows, item):
            total += item["x"] + item["m"] + item["a"] + item["s"]
    return total

def modify_range(cond, ranges, invert=False):
    if not cond: return
    val = cond[0]

    op = cond[1]
    if invert:
        op = "<=" if op == ">" else ">="

    if op == "<":
        ranges[val][1] = min(ranges[val][1], int(cond[2:]) - 1)
    elif op == "<=":
        ranges[val][1] = min(ranges[val][1], int(cond[2:]))
    elif op == ">=":
        ranges[val][0] = max(ranges[val][0], int(cond[2:]))
    else:
        ranges[val][0] = max(ranges[val][0], int(cond[2:]) + 1)

# backtracking
def recurse(workflows, workflow, ranges, results):
    if workflow == "R":
        return
    elif workflow == "A":
        results += [copy.deepcopy(ranges)]
        return

    for cond, to in workflows[workflow]:
        range_copy = copy.deepcopy(ranges)
        modify_range(cond, range_copy)
        recurse(workflows, to, range_copy, results)
        # everytime we fail a condition, we invert the last range for next iteration
        modify_range(cond, ranges, invert=True)

def solution2(workflows, items):
    total = 0
    # find all chains that lead to an A
    results = []
    ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    recurse(workflows, "in", ranges, results)
    for res in results:
        subTotal = 1
        for item in res.values():
            subTotal *= item[1] - item[0] + 1
        total += subTotal
    return total

if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day19/input1.txt", "r")]
    workflows, items = parse(data)
    print(solution(workflows, items))
    print(solution2(workflows, items))



