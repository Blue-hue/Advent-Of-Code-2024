import numpy as np
import re

def solve_linear_system(a, b, p):
    ans = 0
    A = np.array([a,b]).T
    R = np.linalg.solve(A, p)
    x = round(R[0])
    y = round(R[1])
    if x*a[0] + y*b[0] == p[0] and x*a[1] + y*b[1] == p[1]:
        ans = (3*x + y)
    return ans

with open(r"day13\\input.txt") as f:
    data = f.read().strip().split('\n\n')
    ans1 = ans2 = 0
    for g in data:
        a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", g)[0]))
        b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", g)[0]))
        c = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", g)[0]))
        d = [c[0]+10000000000000, c[1]+10000000000000]
        ans1 += solve_linear_system(a, b, c)
        ans2 += solve_linear_system(a, b, d)
print(ans1, ans2)
