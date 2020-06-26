from collections import Counter
def majorityElement(nums):
    cnt = Counter()
    for i in range(len(nums)):
        cnt[nums[i]]+=1
        if len(cnt)>3:
            cnt -= Counter(set(cnt))
    res = [i for i in cnt if nums.count(i) > len(nums)/3 ]
    return res

# without Counter
# Boyer-Moore Majority Vote algorithm
def majorityElement2(nums):
    cnt1,cnt2=0, 0
    candidate1, candidate2 = None, None
    for i in range(len(nums)):
        if nums[i]==candidate1:
            cnt1+=1
        elif nums[i]==candidate2:
            cnt2+=1
        elif cnt2 == 0:
            candidate2,cnt2=nums[i],1
        elif cnt1 == 0:
            candidate1,cnt1=nums[i],1
        else:
            cnt1-=1
            cnt2-=1
    return [i for i in [candidate1,candidate2] if nums.count(i)>len(nums)/3]


if __name__ == "__main__":
    nums = [1,1,1,3,3,2,2,2]
    print (majorityElement2(nums))

    