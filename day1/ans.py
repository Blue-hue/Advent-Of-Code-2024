from collections import Counter
f1 = open("day1\\input.txt", "r")
lst1 = []
lst2 = []
lines = f1.readlines()
for line in lines:
    a,b = line.split()
    lst1.append(int(a))
    lst2.append(int(b))

#PART1
# lst1.sort()
# lst2.sort()
# ans = 0
# for i in range(len(lst1)):
#     ans += abs(lst1[i]-lst2[i])
# print(ans)

#PART2
c2 = Counter(lst2)
ans = 0
for num in lst1:
    ans += num * c2[num]
print(ans)