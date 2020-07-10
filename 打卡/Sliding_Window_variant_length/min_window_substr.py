from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        filterd_s = []

        for i, char in enumerate(s):
            if char in dict_t:
                filterd_s.append((i,char))

        l,r = 0,0
        formed = 0
        windows_count = {}
        ans = float("inf"),None,None
        while r<len(filterd_s):
            character = filterd_s[r][1]
            windows_count[character] = windows_count.get(character,0) + 1
            if windows_count[character] == dict_t[character]:
                formed += 1

            while l<=r and formed ==required:
                character = filterd_s[l][1]
                end = filterd_s[r][0]
                start = filterd_s[l][0]
                if end-start+1<ans[0]:
                    ans = (end-start+1,start,end)
                
                windows_count[character] -= 1
                if windows_count[character]<dict_t[character]:
                    formed -= 1
                l+=1
            r+=1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


