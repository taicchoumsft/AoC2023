
def solution(data):
    time = map(int, data[0].split(":")[1].split())
    distance = map(int, data[1].split(":")[1].split())

    total = 1
    for t, d in zip(time, distance):
        # i represents how much time we hold down
        # for i in range(1, t):
        #     distance_travelled = i * (t - i)
        #     if distance_travelled > d:
        #         distance += [distance_travelled]

        total *= len([i * (t - i) for i in range(1, t) if i * (t - i) > d])

    return total


if __name__ == "__main__":
    data = []
    with open("input2.txt", "r") as file:
        data = file.readlines()

    print(solution(data))