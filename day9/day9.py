

def parse(data):
    arrs = []
    for line in data:
        arrs += [[int(x) for x in line.split()]]
    return arrs

def process_tree(arr):
    diffs = [arr]

    while any(diffs[-1]):
        diffs += [[j - i for i, j in zip(diffs[-1][:-1], diffs[-1][1:])]]

    return diffs

def calculate_next(diffs, left = False):
    prev = 0

    for i in range(len(diffs) - 2, -1, -1):
        if left:
            prev = diffs[i][0] - prev
        else:
            prev += diffs[i][-1]

    return prev

def solution(data, left = False):
    arrs = parse(data)

    nexts = []
    for arr in arrs:
        diffs = process_tree(arr)
        next = calculate_next(diffs, left)
        nexts += [next]
    return sum(nexts)

if __name__ == "__main__":
    data = [line for line in open("input1.txt", "r")]
    print(solution(data))
    print(solution(data, left=True))

