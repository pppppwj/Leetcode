class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        aux_nums = []
        aux_indexs = []
        
        def window_append(i):
            if not aux_nums or aux_nums[-1]>=nums[i]:
                aux_nums.append(nums[i])
                aux_indexs.append(i)
            else:
                while (aux_nums and aux_nums[-1]<nums[i]):
                    aux_nums.pop()
                    aux_indexs.pop()
                aux_nums.append(nums[i])
                aux_indexs.append(i) 
                
        for i in range(k):
            window_append(i)
        
        res.append(aux_nums[0])
        
        for i in range(k,len(nums)):
            if aux_indexs[0] == i-k:
                aux_indexs.pop(0)
                aux_nums.pop(0)
            window_append(i)
            res.append(aux_nums[0])
        
        return res
            