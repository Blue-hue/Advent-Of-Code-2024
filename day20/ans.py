import sys
import re
from collections import deque

sys.setrecursionlimit(10**6)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

D = open("day20\\input.txt").read().strip()
G = D.split('\n')
R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr, sc = r, c
        if G[r][c] == 'E':
            er, ec = r, c

DIST = {}
Q = deque([(0, er, ec)])
while Q:
    d, r, c = Q.popleft()
    if (r, c) in DIST:
        continue
    DIST[(r, c)] = d
    for dr, dc in DIRS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#':
            Q.append((d + 1, rr, cc))

def find_cheat(d0, CHEAT_TIME):
    ans = set()
    Q = deque([(0, None, None, None, sr, sc)])
    SEEN = set()
    SAVE = 100
    while Q:
        d, cheat_start, cheat_end, cheat_time, r, c = Q.popleft()
        if d >= d0 - SAVE:
            continue
        if G[r][c] == 'E':
            if cheat_end is None:
                cheat_end = (r, c)
            if d <= d0 - SAVE and (cheat_start, cheat_end) not in ans:
                ans.add((cheat_start, cheat_end))
        if (r, c, cheat_start, cheat_end, cheat_time) in SEEN:
            continue
        SEEN.add((r, c, cheat_start, cheat_end, cheat_time))

        if cheat_start is None:
            Q.append((d, (r, c), None, CHEAT_TIME, r, c))
        if cheat_time is not None and G[r][c] != '#':
            if DIST[(r, c)] <= d0 - 100 - d:
                ans.add((cheat_start, (r, c)))
        if cheat_time == 0:
            continue
        else:
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if cheat_time is not None:
                    if 0 <= rr < R and 0 <= cc < C:
                        Q.append((d + 1, cheat_start, None, cheat_time - 1, rr, cc))
                else:
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#':
                        Q.append((d + 1, cheat_start, cheat_end, cheat_time, rr, cc))
    return len(ans)

d0 = DIST[(sr, sc)]
print(find_cheat(d0, 2))
print(find_cheat(d0, 20))