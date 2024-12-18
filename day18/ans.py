from collections import deque

def shortest_path(grid):
    n, m = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if grid[0][0] == '#' or grid[n-1][m-1] == '#':
        return -1
    queue = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (n-1, m-1):
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1

f = open("day18\\input.txt").read().strip().split('\n')
grid = [[0 for _ in range(71)] for _ in range(71)]

for i in range(1024):
    x,y = [int(x) for x in f[i].split(',')]
    grid[x][y] = '#'
print(shortest_path(grid))

for i in range(1024,len(f)):
    x,y = [int(x) for x in f[i].split(',')]
    grid[x][y] = '#'
    if shortest_path(grid)==-1:
        print(x,y)
        break