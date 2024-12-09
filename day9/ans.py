line = open(r"day9\\input.txt", "r").read().strip()
# line = "2333133121414131402"

def formatline(line):
    n = len(line)
    s = []
    id = 0
    for i in range(n):
        if i%2==0:
            s.extend([id]*int(line[i]))
            id += 1
        else:
            s.extend(['.']*int(line[i]))
    return s
formatted = formatline(line)

def findspace(formatted, idlen):
    c = 0
    for i in range(len(formatted)):
        if formatted[i]=='.':
            c += 1
            if c == idlen:
                return i - idlen + 1
        else:
            c = 0
    return -1

#PART1
# while i < j:
#     while formatted[i] != '.' and i < j:
#         i += 1
#     while j > i and formatted[j]=='.':
#         j -= 1
#     formatted[i], formatted[j] = formatted[j], formatted[i]
# print(formatted)

#PART2
idblock = []
pref = [0]
cur = 0
for i in range(len(line)):
    cur += int(line[i])
    pref.append(cur)
    if i%2==0:
        idblock.append(int(line[i]))

for i in range(len(idblock) - 1, -1, -1):
    idlen = idblock[i]
    ididx = pref[2*i]
    spaceidx = findspace(formatted, idlen)
    if spaceidx == -1 or spaceidx >= ididx:
        continue
    for k in range(idlen):
        formatted[k + spaceidx], formatted[k + ididx] = formatted[k + ididx], formatted[k + spaceidx]

ans = 0
for i in range(len(formatted)):
    if formatted[i]!='.':
        ans += formatted[i]*i
print(ans)
