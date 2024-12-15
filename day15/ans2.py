from collections import deque

grid, commands = open("day15\\input.txt").read().strip().split('\n\n')
grid = [list(x) for x in grid.strip().split('\n')]
commands = commands.replace('\n','')
m,n = len(grid), len(grid[0])

def solve(grid):
    R, C = len(grid), len(grid[0])
    biggrid = []
    for r in range(R):
        row = []
        for c in range(C):
            if grid[r][c]=='#':
                row.append('#')
                row.append('#')
            if grid[r][c]=='O':
                row.append('[')
                row.append(']')
            if grid[r][c]=='.':
                row.append('.')
                row.append('.')
            if grid[r][c]=='@':
                row.append('@')
                row.append('.')
        biggrid.append(row)
    grid = biggrid
    C *= 2

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@':
                sr,sc = r,c
                grid[r][c] = '.'

    dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    r,c = sr,sc
    for cmd in commands:
        dr,dc = dirs[cmd]
        rr,cc = r+dr,c+dc
        if grid[rr][cc]=='#':
            continue
        elif grid[rr][cc]=='.':
            r,c = rr,cc
        elif grid[rr][cc] in ['[', ']']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if grid[rrr][ccc]=='#':
                    ok = False
                    break
                if grid[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    Q.append((rrr,ccc+1))
                if grid[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    Q.append((rrr,ccc-1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        grid[rrr][ccc] = grid[rr][cc]
                        grid[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc
    return grid

ans = 0
grid = solve(grid)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c]=='[':
            ans += 100*r+c
print(ans)