from collections import defaultdict, deque

def score(arr,mp):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] in mp[arr[j]]:
                return 0
    return arr[n//2]

#added later
def toposort(arr, mp):
    graph = defaultdict(set)
    in_degree = {x: 0 for x in arr}

    for u in arr:
        for v in arr:
            if v in mp[u]:
                graph[u].add(v)
                in_degree[v] += 1

    queue = deque([node for node in arr if in_degree[node] == 0])
    res = []

    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return res

def arrange(arr, mp):
    st = set(arr)
    res = []
    while st:
        to_remove = set()
        for x in st:
            if all(y not in mp[x] for y in st if x != y):
                res.append(x)
                to_remove.add(x)
        st -= to_remove
    return res

rules, lines = open(r"day5\\input.txt", "r").read().split("\n\n")
d = defaultdict(set)
for rule in rules.split("\n"):
    a,b = [int(x) for x in rule.split('|')]
    d[a].add(b)

ans1 = ans2 = ans3 = 0
for line in lines.split("\n"):
    arr = list(map(int,line.split(",")))
    ans1 += score(arr,d)
    if score(arr,d)==0:
        ans2 += toposort(arr,d)[len(arr)//2]
        ans3 += arrange(arr,d)[len(arr)//2]


print(ans1, ans2, ans3)