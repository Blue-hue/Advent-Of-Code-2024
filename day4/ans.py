def valid_square(i,j,m,n):
    return 0 <= i < m and 0 <= j < n

def findWord(grid, m, n, word, idx, i, j, dirX, dirY):
    if idx == len(word):
        return True

    if valid_square(i,j,m,n) and word[idx] == grid[i][j]:
        return findWord(grid, m, n, word, idx + 1, i + dirX, j + dirY, dirX, dirY)
    
    return False

def searchWord(grid, word):
    ans = 0
    st = set()
    m = len(grid)
    n = len(grid[0])
    # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)] #PART1
    dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]                                         #PART2
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0]:  
                for dirX, dirY in dirs:
                    if findWord(grid, m, n, word, 0, i, j, dirX, dirY):
                        # ans += 1                  #PART1
                        if (i+dirX,j+dirY) in st:   #PART2
                            ans += 1                #PART2
                        st.add((i+dirX, j+dirY))    #PART2
    return ans

f = [list(line) for line in open(r"day4\\input.txt","r").read().split('\n')]
# print(f)

ans = searchWord(f,"MAS")
print(ans)