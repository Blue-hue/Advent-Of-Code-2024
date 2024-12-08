from collections import defaultdict
import itertools
import math

grid = [list(x) for x in open(r"day8\\input.txt", "r").read().strip().split('\n')]
d = defaultdict(list)
m = len(grid)
n = len(grid[0])

for i in range(m):
    for j in range(n):
        if grid[i][j] != '.':
            d[grid[i][j]].append([i, j])

ans = set()
for lst in d.values():
    combs = itertools.permutations(lst, 2)
    for comb in combs:
        difx = comb[0][0] - comb[1][0]
        dify = comb[0][1] - comb[1][1]
        gcdcc = math.gcd(difx, dify)
        difx = difx // gcdcc
        dify = dify // gcdcc
        x, y = comb[1][0], comb[1][1]
        while 0 <= x + difx < m and 0 <= y + dify < n:
            x += difx
            y += dify
            ans.add((x, y))

print(len(ans))
