from collections import deque

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
ans1 = 0
ans2 = 0
f = open(r"day12\\input.txt").read().strip()

grid = f.split('\n')
rows = len(grid)
cols = len(grid[0])

vis = set()
for r in range(rows):
    for c in range(cols):
        if (r,c) in vis:
            continue
        queue = deque([(r,c)])
        area = 0
        perim = 0
        PERIM = {}
        while queue:
            r2,c2 = queue.popleft()
            if (r2,c2) in vis:
                continue
            vis.add((r2,c2))
            area += 1
            for dr,dc in dirs:
                rr = r2+dr
                cc = c2+dc
                if 0<=rr<rows and 0<=cc<cols and grid[rr][cc]==grid[r2][c2]:
                    queue.append((rr,cc))
                else:
                    perim += 1
                    if (dr,dc) not in PERIM:
                        PERIM[(dr,dc)] = set()
                    PERIM[(dr,dc)].add((r2,c2))

        sides = 0
        for dir,lst in PERIM.items():
            SEEN_PERIM = set()
            for (pr,pc) in lst:
                if (pr,pc) not in SEEN_PERIM:
                    sides += 1
                    queue = deque([(pr,pc)])
                    while queue:
                        r2,c2 = queue.popleft()
                        if (r2,c2) in SEEN_PERIM:
                            continue
                        SEEN_PERIM.add((r2,c2))
                        for dr,dc in dirs:
                            rr,cc = r2+dr,c2+dc
                            if (rr,cc) in lst:
                                queue.append((rr,cc))

        ans1 += area*perim
        ans2 += area*sides

print(ans1)
print(ans2)