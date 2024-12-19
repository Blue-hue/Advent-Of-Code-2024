def counter(towel_patterns, designs):
    def designok(design, patterns):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for pattern in patterns:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern and dp[i - len(pattern)]:
                    dp[i] = 1
                    break
        return dp[n]

    patterns = towel_patterns.split(", ")
    designs = designs.strip().splitlines()
    res = 0
    for design in designs:
        res += designok(design, patterns)
    return res

with open("day19\\input.txt") as f:
    towel_patterns, designs = f.read().split('\n\n')
    print(counter(towel_patterns, designs))