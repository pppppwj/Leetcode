class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # check "A"
        res = 0
        for index in range(26):
            check = chr(ord("A") + index)

            i = j = 0
            tmp = 0
            cnt = k
            while(j<len(s)):
                if s[j] != check:
                    if cnt > 0:
                        cnt -= 1
                    else:
                        tmp = tmp if tmp>j-i else j-i
                        while(s[i] == check):
                            i += 1
                        i += 1
                j+=1
            tmp = tmp if tmp>j-i else j-i
            
            res = res if res >= tmp else tmp
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s,k))
