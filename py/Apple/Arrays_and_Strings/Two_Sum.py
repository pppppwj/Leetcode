# brute force
# speed : O(n^2)
# space : O(1)


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

# hashmap
# speed : O(n)
# space : O(n)


def twoSum2(nums, target):
    res = {}
    for i in range(len(nums)):
        if nums[i] in res:
            return [i, res[nums[i]]]
        else:
            res[target-nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum2(nums, target))
