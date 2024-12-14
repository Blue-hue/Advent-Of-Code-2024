import re

WIDTH = 101
HEIGHT = 103
robots = []
totalrobots = 500
for line in open(r"day14\\input.txt").read().strip().split('\n'):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

tl = bl = tr = br = 0
ymid = (HEIGHT - 1) // 2
xmid = (WIDTH - 1) // 2

for i in range(1,100000):
    seen = set()
    for x, y, vx, vy in robots:
        newx = (x + vx * i) % WIDTH
        newy = (y + vy * i) % HEIGHT
        # if newx == xmid or newy == ymid: continue
        # if newx < xmid:
        #     if newy < ymid:
        #         tl += 1
        #     else:
        #         bl += 1
        # else:
        #     if newy < ymid:
        #         tr += 1
        #     else:
        #         br += 1
        seen.add((newx,newy))
    if len(seen)==totalrobots:
        print(i)
        break

# print(tl * bl * tr * br)
