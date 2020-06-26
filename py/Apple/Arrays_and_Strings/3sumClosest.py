def ThreeSumClosest(nums,target):
    nums = sorted(nums)
    res = nums[0]+nums[1]+nums[-1]
    diff = abs(target-res)
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while (j<k):
            currsum = nums[i] + nums[j] + nums[k]
            if currsum>target:
                k-=1
            elif currsum<target:
                j+=1
            else: return target
            
            if abs(currsum-target)<diff:
                diff = abs(currsum-target)
                res = currsum

    return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(ThreeSumClosest(nums,target))