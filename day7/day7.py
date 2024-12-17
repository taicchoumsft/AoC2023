from collections import Counter
import functools

def compare(h1, h2, relative_strength_fn, adjust_jokers):
    def rank(hand):
        cnt = Counter(hand)

        if adjust_jokers:
            joker_counts = cnt['J']
            if joker_counts == 5: return 7
            del cnt['J']
            cnt[cnt.most_common(1)[0][0]] += joker_counts

        counts = [a[1] for a in cnt.most_common()]

        #python 3.10 match case
        match counts:
            case [5]: return 7 # 5 of a kind
            case [4, 1]: return 6 # 4 of a kind
            case [3, 2]: return 5 # Full house
            case [3, *_]: return 4 # Three of a kind
            case [2, 2, 1]: return 3 # two pairs
            case [2, *_]: return 2 # one pair
            case _: return 1 # high card

    r1, r2 = rank(h1[0]), rank(h2[0])
    if (r1 > r2): return 1
    elif (r1 < r2): return -1

    for ch1, ch2 in zip(h1[0], h2[0]):
        if relative_strength_fn(ch1) > relative_strength_fn(ch2): return 1
        elif relative_strength_fn(ch1) < relative_strength_fn(ch2): return -1
    return 0 # no-op

def solution(data, relorder, adjust_jokers):
    cards = [line.split() for line in data]

    relative_strength = lambda ch: relorder.index(ch)

    cards.sort(key=functools.cmp_to_key(lambda x, y: compare(x, y, relative_strength, adjust_jokers)))

    return sum(idx * int(bid) for idx, (_, bid) in enumerate(cards, 1))

if __name__ == "__main__":
    data = [line for line in open("input1.txt", "r")]
    assert solution(data, "23456789TJQKA", False) == 250120186
    assert solution(data, "J23456789TQKA", True) == 250665248

