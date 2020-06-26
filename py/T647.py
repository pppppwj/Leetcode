class Solution:
    def countSubstrings(self, s: str) -> int:

        # Method 1 ： center O(n^2)
        # count=0
        # for i in range(2*len(s)-1):
        #     left = i//2
        #     right = left + i%2
        #     while left>=0 and right<len(s) and s[left]==s[right]:
        #         count+=1
        #         left-=1
        #         right+=1
        # return count


        #Method 2 : Manacher's Algorithm
        def manacher(s):
            s = '#'+'#'.join(s)+'#'
            p = [0]*len(s)
            center = 0
            r = 0
            for i in range(1,len(s)-1):
                i_mirror = 2*center - i
                if r>i:
                    p[i]=min(p[i_mirror],r-i)
                while i+p[i]+1<len(s) and i-p[i]-1>-1 and s[i+p[i]+1]==s[i-p[i]-1]:
                    p[i]+=1
                if i+p[i]>r:
                    center,r=i,i+p[i]
            return p
        print(manacher(s))
        return sum([(i+1)//2 for i in manacher(s)] )



T="aaa"
sol=Solution()
print(sol.countSubstrings(T))