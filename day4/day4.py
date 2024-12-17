from collections import defaultdict

def solution(data):
    total = 0
    mp = defaultdict(int)

    for line in data:
        cardNo, rest = line.split(":")
        cardNum = int(cardNo.split(" ")[-1])

        winning_str, have_str = rest.split("|")
        winning = winning_str.strip().split(" ")
        have = have_str.strip().split(" ")

        winning = [winning for winning in winning if winning != ""]
        have = [have for have in have if have != ""]

        winning_set = set(winning)
        have_set = set(have)
        count = len(winning_set & have_set)
        if count > 0:
            total += 2 ** (count - 1)
        mp[cardNum] = count

    # diff array, O(1) write, O(n) read, read once
    diff = [0] * (len(data) + 1)
    diff[0] = 1
    diff[-1] = -1

    cur_level = 1
    for i in range(len(data)):
        w = mp[i + 1]
        if i > 0:
            cur_level += diff[i]
        diff[i + 1] += cur_level
        diff[i + 1 + w] -= cur_level

    for i in range(1, len(data) + 1):
        diff[i] += diff[i - 1]

    return total, sum(diff)

if __name__ == "__main__":
    data = []
    with open("input1.txt", "r") as file:
        data = file.readlines()

    print(solution(data))