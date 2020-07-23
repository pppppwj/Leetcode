class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        res = float("-inf")
        resl = resr = -1
        print(s)
        for i in range(len(s)):
            cnt = 1
            while i >= cnt and i+cnt <= len(s) - 1 and s[i - cnt] == s[i + cnt]:
                cnt += 1
            if cnt>res:
                resl, resr = i-cnt+1, i+cnt-1
                res = cnt
        return s[resl:resr].replace("#","")
    
    def Manacher(self,s):
        s = "#" + "#".join(s) + "#"
        radius = [0]*len(s)
        maxRight = 0
        center = 0
        maxRadius = 0
        maxRadiusCenter = 0
        for i in range(len(s)):
            if i < maxRight:
                radius[i] = min(maxRight-i,radius[2*center - i])
            else:
                radius[i] = 1
            while i-radius[i] > -1 and i+radius[i] < len(s) and s[i-radius[i]] == s[i+radius[i]]:
                radius[i] += 1
            
            if i+radius[i]-1 > maxRight:
                maxRight = i + radius[i]-1
                center = i
            
            if radius[i] > maxRadius:
                maxRadius = radius[i]
                maxRadiusCenter = i
        
        return s[maxRadiusCenter-maxRadius+1:maxRadiusCenter+maxRadius-1].replace("#","")

        

if __name__ == "__main__":
    s = "abc"
    ss = "#".join(s)
    print(ss)
