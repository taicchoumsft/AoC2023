

# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements

def parse(data):
    for line in data:
        p, v = line.split()
        v = [int(n) for n in v.split(",")]
        yield p, v

def backtrack(p, v, p_idx):
    if p_idx == len(p):
        c_idx = 0
        v_idx = 0
        while c_idx < len(p):
            if p[c_idx] == ".":
                c_idx += 1
                continue

            cnt = 0
            while c_idx < len(p) and p[c_idx] == "#":
                cnt += 1
                c_idx += 1

            if v_idx < len(v) and v[v_idx] != cnt:
                return 0
            v_idx += 1
        return 1 if v_idx == len(v) else 0

    total = 0
    if p[p_idx] == "?":
        p[p_idx] = "."
        total += backtrack(p, v, p_idx+1)
        p[p_idx] = "#"
        total += backtrack(p, v, p_idx+1)
        p[p_idx] = "?"
    else:
        total += backtrack(p, v, p_idx+1)

    return total

def solution(data):
    total = 0
    for p, v in parse(data):
        result = backtrack(list(p), v, 0)
        print(p, v, result)
        total += result
    return total

def solution2(data):
    #@lru_cache
    def backtrack(p_idx, v_idx):
        if p_idx >= len(p):
            return 1 if v_idx == len(v) else 0

        if v_idx >= len(v):
            return 0 if "#" in p[p_idx:] else 1

        if p[p_idx] != ".":
            # ? or # case
            notake = 0
            if p[p_idx] == "?":
                notake = backtrack(p_idx + 1, v_idx)

            target = v[v_idx]
            while p_idx < len(p) and p[p_idx] != "." and target > 0:
                target -= 1
                p_idx += 1

            if (p_idx < len(p) and p[p_idx] == "#" and target == 0) or target > 0: return notake
            return backtrack(p_idx + 1, v_idx + 1) + notake

        else:
            #"." case
            return backtrack(p_idx + 1, v_idx)

    total = 0
    for p, v in parse(data):
        p = list("?".join([p for i in range(5)]))
        v = v * 5
        result = backtrack(0, 0)
        print("".join(p), v, result)
        total += result
    return total

if __name__ == "__main__":
    data = [line for line in open("/Users/chou/source/workspace/aoc2023/day12/sample1.txt", "r")]
    print(solution2(data))

