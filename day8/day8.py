from collections import defaultdict
import functools
from math import lcm

def parse(data):
    path = data[0].strip()
    ends_with_a = []

    mp = defaultdict(tuple)
    for line in data[2:]:
        k, v = line.split(" = ")
        l, r = v[1:-2].split(",")
        mp[k] = (l.strip(), r.strip())
        if k.endswith("A"): ends_with_a += [k]

    return path, mp, ends_with_a

def path_to_zz(mp, cur, path):
    cnt = 0
    idx = 0
    while not cur.endswith("Z"):
        dir = path[idx]
        if dir == "L":
            cur = mp[cur][0]
        else:
            cur = mp[cur][1]

        cnt += 1
        idx += 1
        if idx == len(path):
            idx = 0
    return cnt

def solution(data):
    path, mp, _ = parse(data)
    return path_to_zz(mp, "AAA", path)

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(*args):
    def lcmi(a, b):
        return (a * b) // gcd(a, b)
    return functools.reduce(lcmi, args)

def solution2(data):
    path, mp, ends_with_a = parse(data)
    costs = [path_to_zz(mp, item, path) for item in ends_with_a]
    return lcm(*costs)

if __name__ == "__main__":
    data = [line for line in open("input1.txt", "r")]
    print(solution(data))
    print(solution2(data))
