def ok(arr)->bool:
    n = len(arr)
    flag = True
    for i in range(n-1):
        if 1<= abs(arr[i]-arr[i+1]) <=3: continue
        else:
            flag = False
            break
    return flag


f = open("day2\\input.txt", "r").readlines()
ans = 0
for line in f:
    nums = [int(x) for x in line.split()]

    #PART1
    # if sorted(nums)==nums or sorted(nums, reverse=True)==nums:
    #     n = len(nums)
    #     flag = True
    #     for i in range(n-1):
    #         if 1<= abs(nums[i]-nums[i+1]) <=3:
    #             continue
    #         else:
    #             flag = False
    #     if flag:
    #         ans += 1

    #PART2
    n = len(nums)
    for i in range(n):
        newnums = nums[0:i] + nums[i+1:]
        if sorted(newnums)==newnums or sorted(newnums,reverse=True)==newnums:
            if ok(newnums):
                ans += 1
                break
print(ans)
