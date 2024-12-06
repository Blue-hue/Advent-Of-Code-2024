grid = [list(x) for x in open(r"day6\\input.txt", "r").read().split('\n')]
m = len(grid)
n = len(grid[0])
st = set()
posx = posy = 0

found = False
for i in range(m):
    for j in range(n):
        if grid[i][j]=='^':
            posx = i
            posy = j
            found = True
            break
    if found:
        break

dirx = [-1,0,1,0]
diry = [0,1,0,-1]
idx = 0

def valid(i,j,m,n):
    return 0<=i<m and 0<=j<n

while valid(posx,posy,m,n) and valid(posx + dirx[idx], posy + diry[idx], m, n):
    if grid[posx+dirx[idx]][posy+diry[idx]]!='#':
        st.add((posx,posy))
        posx += dirx[idx]
        posy += diry[idx]
    else:
        idx = (idx+1)%4
st.add((posx,posy))
print(len(st))