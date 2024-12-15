grid, commands = open("day15\\input.txt").read().strip().split('\n\n')
grid = [list(x) for x in grid.strip().split('\n')]
# print(grid)

commands = commands.replace('\n','')
m,n = len(grid), len(grid[0])
# print(rx,ry)

dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

def simulate_robot(grid, commands):
    m,n = len(grid), len(grid[0])
    rx = ry = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                rx, ry = i, j
    for cmd in commands:
        dr, dc = dirs[cmd]
        nr, nc = rx + dr, ry + dc
        if not (0 <= nr < m and 0 <= nc < n):
            continue
        if grid[nr][nc] == '#':
            continue
        if grid[nr][nc] == '.':
            grid[nr][nc] = '@'
            grid[rx][ry] = '.'
            rx, ry = nr, nc
            continue
        if grid[nr][nc] == 'O':
            current_r, current_c = nr, nc
            while 0 <= current_r < m and 0 <= current_c < n and grid[current_r][current_c] == 'O':
                current_r += dr
                current_c += dc
            if 0 <= current_r < m and 0 <= current_c < n and grid[current_r][current_c] == '.':
                grid[current_r][current_c] = 'O'
                grid[nr][nc] = '@'
                grid[rx][ry] = '.'
                rx, ry = nr,nc
            continue
    return grid

newg = simulate_robot(grid,commands)
ans = 0
for i in range(m):
    for j in range(n):
        if newg[i][j] == 'O':
            ans += (100*i + j)
print(ans)
