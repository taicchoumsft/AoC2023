from collections import defaultdict
import heapq
import random

def parse(lines):
    adj_list = defaultdict(list)
    for line in lines:
        node, nbrs = line.split(": ")
        nbrs = nbrs.split(" ")
        adj_list[node] += nbrs
        for nbr in nbrs:
            adj_list[nbr] += [node]

    adj_matrix = [[0 for _ in range(len(adj_list))] for _ in range(len(adj_list))]

    node_to_idx = {}
    for i, node in enumerate(adj_list):
        node_to_idx[node] = i

    for node, nbrs in adj_list.items():
        for nbr in nbrs:
            adj_matrix[node_to_idx[node]][node_to_idx[nbr]] = 1
            #adj_matrix[node_to_idx[nbr]][node_to_idx[node]] = 1

    return adj_list, adj_matrix, node_to_idx


def cut_phase(adj_matrix):
    n = len(adj_matrix)
    s = []
    seen = set()
    cut_weights = []

    q = [(-1, 0)]

    while q:
        weight, node = heapq.heappop(q)
        weight = -weight

        if node in seen:
            continue

        s += [node]
        seen.add(node)
        cut_weights += [weight]

        for i, w in enumerate(adj_matrix[node]):
            if w > 0 and i not in seen:
                # must combine the weights of the edges from the cut to the s supernode
                new_weight = sum([adj_matrix[i][j] for j in s])
                heapq.heappush(q, (-new_weight, i))

    return s[-2], s[-1], cut_weights[-1]

    # cut_weights = []
    # n = len(adj_matrix)
    # s = [n - 1]
    # candidates = set(range(n - 1))
    # cut_weights = []

    # while candidates:
    #     mx = float("-inf")
    #     nxt = -1

    #     for c in candidates:
    #         weight = 0
    #         for i in s:
    #             if adj_matrix[i][c] > 0:
    #                 weight += adj_matrix[i][c]
    #         if weight > mx:
    #             mx = weight
    #             nxt = c

    #     candidates.remove(nxt)
    #     s += [nxt]
    #     cut_weights += [mx]
    # print(s, cut_weights)
    # return s[-2], s[-1], cut_weights[-1]

# super slow implementation
def stoer_wagner(adj_matrix):
    orig_size = len(adj_matrix)
    print("num components", orig_size)
    min_cut = float("inf")
    t_partition = []

    while len(adj_matrix) > 1:
        #print(len(adj_matrix))
        s, t, cut_size = cut_phase(adj_matrix)
        t_partition += [t]

        if cut_size < min_cut:
            min_cut = cut_size
            print(min_cut, len(t_partition) * (orig_size - len(t_partition)))
            print(len(t_partition), orig_size - len(t_partition))

        # adj_matrix[s][t] = 0
        # adj_matrix[t][s] = 0
        for i in range(len(adj_matrix)):
            adj_matrix[s][i] += adj_matrix[t][i]
            adj_matrix[i][s] += adj_matrix[t][i]
            adj_matrix[t][i] = 0
            adj_matrix[i][t] = 0

        adj_matrix.pop(t)
        for row in adj_matrix:
            row.pop(t)

    return min_cut

if __name__ == "__main__":
    data = [line.strip() for line in open("./input1.txt", "r")]
    adj_list, adj_matrix, node_to_idx = parse(data)
    stoer_wagner(adj_matrix)