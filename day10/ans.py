from collections import deque

grid = [list(map(int, row)) for row in open(r"day10\\input.txt", "r").read().strip().split('\n')]
rows, cols = len(grid), len(grid[0])

#PART1
def bfs(i, j):
    visited = set()
    queue = deque([(i, j, grid[i][j])])
    visited.add((i, j))
    res = 0

    while queue:
        x, y, value = queue.popleft()
        if grid[x][y] == 9:
            res += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == value + 1:
                    queue.append((nx, ny, grid[nx][ny]))
                    visited.add((nx, ny))
    return res

# PART2
memo = {}
def count_unique_paths(x, y, value):
    if grid[x][y] == 9:
        return 1
    if (x, y) in memo:
        return memo[(x, y)]
    res = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == value + 1:
            res += count_unique_paths(nx, ny, grid[nx][ny])
    memo[(x, y)] = res
    return res

ans1 = ans2 = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            ans1 += bfs(i, j)
            ans2 += count_unique_paths(i, j, 0)
print(ans1, ans2)