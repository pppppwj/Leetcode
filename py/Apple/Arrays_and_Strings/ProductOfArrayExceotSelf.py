class Solution:
    def productExceptSelf(self, nums):
        # return sol (no more extra space)
        sol = [1]*len(nums)
        l=1
        for i in range(1,len(nums)):
            l*=nums[i-1]
            sol[i]*=l
        r=1
        for i in range(len(nums)-2,-1,-1):
            r*=nums[i+1]
            sol[i]*=r
        return sol


if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print (sol.productExceptSelf(nums))