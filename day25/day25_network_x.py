import networkx as nx

g = nx.Graph()

# solution copied from reddit user /u/askalski
for line in open("./input1.txt", "r").readlines():
    source, raw_targets = line.rstrip().split(": ")
    targets = raw_targets.split(" ")
    for target in targets:
        g.add_edge(source, target, capacity=1)


cut_val, partitions = nx.stoer_wagner(g)
print(cut_val, len(partitions[0]), len(partitions[1]), (len(partitions[0]) * len(partitions[1])))