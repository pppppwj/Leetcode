class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # segments 
        for c in set(s):
            if s.count(c) < k:
                segs = s.split(c)
            
                max_len = 0
                for seg in segs:

                    cur_len = self.longestSubstring(seg,k)
                    max_len = max(max_len, cur_len)
            
                return max_len
        return len(s)
if __name__ == "__main__":
    test = "aaabb"
    sol = Solution()
    print(sol.longestSubstring(test,3))
