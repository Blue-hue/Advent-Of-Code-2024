grid = [list(x) for x in open(r"day6\\input.txt", "r").read().split('\n')]
m = len(grid)
n = len(grid[0])
posx = posy = 0

found = False
for i in range(m):
    for j in range(n):
        if grid[i][j] == '^':
            posx = i
            posy = j
            found = True
            break
    if found:
        break

idx = 0
sr, sc = posx, posy

def valid(i, j, m, n):
    return 0 <= i < m and 0 <= j < n

ans = 0
for o_x in range(m):
    for o_y in range(n):
        posx, posy = sr, sc
        idx = 0
        SEEN = set()
        SEEN_POS = set()

        while True:
            if (posx, posy, idx) in SEEN:
                ans += 1
                break

            SEEN.add((posx, posy, idx))

            dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][idx]
            nextx = posx + dr
            nexty = posy + dc

            if not (0 <= nextx < m and 0 <= nexty < n):
                break

            if grid[nextx][nexty] == '#' or (nextx == o_x and nexty == o_y):
                idx = (idx + 1) % 4
            else:
                posx, posy = nextx, nexty

print(ans)