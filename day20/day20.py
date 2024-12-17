from collections import defaultdict

# model as a graph that has state

def parse(data):
    rules = {}

    conjunctions = defaultdict() # track inputs for conjunctions
    flipflops = {} # track state for flipflops

    for line in data:
        sender, receivers = line.split("->")
        sender = sender.strip()
        type = None, None
        if sender.startswith("%") or sender.startswith("&"):
            type = sender[0]
            sender = sender[1:]

            if type == "&":
                conjunctions[sender] = defaultdict(bool)
            elif type == "%":
                flipflops[sender] = False

        receivers = [receiver.strip() for receiver in receivers.split(",")]
        rules[sender] = receivers

    for sender, receivers in rules.items():
        for receiver in receivers:
            if receiver in conjunctions:
                conjunctions[receiver][sender] = False

    return rules, conjunctions, flipflops

def full_cycle(rules, conjunction_inputs, flip_flops, cycles):
    # model as a graph, perform a BFS - start at broadcast node and send a low pulse
    low_pulses = 0
    high_pulses = 0
    button_presses = 0

    q = [(None, "broadcaster", False)]

    while q:
        sz = len(q)
        while sz > 0:
            parent, node, state = q.pop(0)

            if node == "rx" and not state:
                print("Solution 2: ", button_presses)
                break

            if not state:
                low_pulses += 1
            else:
                high_pulses += 1

            sz -= 1

            if node == "broadcaster":
                q += [(node, receiver, False) for receiver in rules[node]]
            elif node in flip_flops and not state:
                flip_flops[node] = not flip_flops[node]
                q += [(node, receiver, flip_flops[node]) for receiver in rules[node]]
            elif node in conjunction_inputs:
                if parent: conjunction_inputs[node][parent] = state

                if all(conjunction_inputs[node].values()):
                   # all inputs high, invert and send low pulse to all receivers
                    q += [(node, receiver, False) for receiver in rules[node]]
                else:
                    # at least one input low, send high pulse to all receivers
                    q += [(node, receiver, True) for receiver in rules[node]]

        if not q:
            q += [(None, "broadcaster", False)]
            button_presses += 1
            if cycles and cycles == button_presses: break
            if button_presses % 1e6 == 0: print(button_presses)

    return low_pulses, high_pulses, button_presses

def solution(rules, conjunction_inputs, flip_flops, cycles = 1000):
    low_pulses, high_pulses, button_presses = full_cycle(rules, conjunction_inputs, flip_flops, cycles)
    return low_pulses * high_pulses

if __name__ == "__main__":
    data = [line.strip() for line in open("/Users/chou/source/workspace/aoc2023/day20/input1.txt", "r")]
    rules, conjunctions, flip_flops = parse(data)
    print(solution(rules, conjunctions, flip_flops, cycles = 1000))
    print(solution(rules, conjunctions, flip_flops, cycles = None))

# 2nd example
# b -> a -> inv -> b -> con
#      |                 ^
#      - - - - - - - - - |

# 653619421 too low
# 654392802 too low