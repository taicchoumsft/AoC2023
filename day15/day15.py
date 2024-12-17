from collections import defaultdict

def parse(data):
    data = "".join(data)
    return data.split(",")

def hash(seq):
    cur = 0

    for ch in seq:
        cur += ord(ch)
        cur *= 17
        cur %= 256

    return cur

def solution(data):
    seq = parse(data)

    total = sum(hash(s) for s in seq)
    return total

def solution2(data):
    seq = parse(data)

    mp = defaultdict(defaultdict)

    for s in seq:
        if "=" in s:
            k, v = s.split("=")
            hash_k = hash(k)
            # because dict remembers insertion order
            mp[hash_k][k] = int(v)

        else:
            k = s[:-1]
            hash_k = hash(k)
            if hash_k in mp:
                if k in mp[hash_k]:
                    del mp[hash_k][k]


    total = 0

    for hash_k, dicts in mp.items():
        for idx, v in enumerate(dicts.values()):
            cur = (int(hash_k) + 1) * (idx + 1) * v
            print(v, cur)
            total += cur

    return total

if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day15/input1.txt", "r")]
    print(solution(data))
    print(solution2(data))
