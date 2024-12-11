from collections import Counter

stones = [int(x) for x in open(r"day11\\input.txt", "r").read().strip().split()]
stones = Counter(stones)
print(stones)

def tracker(stones, blinks):
    for i in range(blinks):
        cur = Counter()
        for stone, count in stones.items():
            if stone == 0:
                cur[1] += count
            elif len(str(stone)) % 2 == 0:
                strstone = str(stone)
                mid = len(strstone) // 2
                left = int(strstone[:mid])
                right = int(strstone[mid:])
                cur[left] += count
                cur[right] += count
            else:
                cur[stone*2024] += count
        stones = cur
    return sum(stones.values())

print(tracker(stones, 25), tracker(stones, 75))
