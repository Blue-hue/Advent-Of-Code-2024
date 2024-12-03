import re
f = open(r"day3\\input.txt", "r").readlines()
f = ''.join(f)

ans = 0
enabled = True

pattern = r"mul\(\d{1,3},\d{1,3}\)"
stop = r"don't\(\)"
resume = r"do\(\)"

final = pattern + '|' + stop + '|' + resume

#PART1
# matches = re.findall(pattern, f)

# PART2
matches = re.findall(final,f)

for s in matches:
    if s == "do()":
        enabled = True
    elif s == "don't()":
        enabled = False
    else:
        if enabled:
            s = s[4:-1]
            a,b = [int(x) for x in s.split(',')]
            ans += a*b

print(ans)