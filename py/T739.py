from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Given a list of daily temperatures T, return a list such that,
        for each day in the input, tells you how many days you would
        have to wait until a warmer temperature. If there is no
        future day for which this is possible, put 0 instead.

        For example,
        input T = [73, 74, 75, 71, 69, 72, 76, 73],
        your output should be [1, 1, 4, 2, 1, 1, 0, 0].
        """

        # O(n^2)
        # res=[0]*len(T)
        # for i in range(len(T)):
        #     for j in range(i+1,len(T)):
        #         if T[j]>T[i]:
        #             res[i]=j-i
        #             break
        #
        # return res

        #stack
        #index from end to 0
        l=len(T)
        ans=[0]*l
        stack=[]
        for i in range(l-1,-1,-1):
            while stack and T[i]>T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans



T = [89,62,70,58,47,47,46,76,100,70]
sol=Solution()
print(sol.dailyTemperatures(T))
