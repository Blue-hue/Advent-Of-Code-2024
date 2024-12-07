f = open("day7\\input.txt", "r").read().strip().split('\n')

def satisfy(nums, i, n, memo=None):
    if memo is None:
        memo = {}
    if i == n - 1:
        return [nums[i]]
    if (i, n) in memo:
        return memo[(i, n)]

    next_results = satisfy(nums, i + 1, n, memo)
    mulval = [nums[i] * x for x in next_results]
    addval = [nums[i] + x for x in next_results]
    concatval = [x * pow(10,len(str(nums[i]))) + nums[i] for x in next_results]
    
    memo[(i, n)] = mulval + addval + concatval
    return memo[(i, n)]

ans1 = 0

for line in f:
    testno, nums = line.split(':')
    testno = int(testno)
    nums = list(map(int, nums.split()))
    print(testno, nums)
    if testno in satisfy(nums[::-1], 0, len(nums)):
        ans1 += testno

print(ans1)