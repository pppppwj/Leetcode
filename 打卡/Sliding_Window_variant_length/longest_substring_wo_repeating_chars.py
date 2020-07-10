class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_substring = set()
        start = i = 0
        res = 0
        while i < len(s):
            if s[i] in set_substring:
                res = res if res > i - start else i - start
                while s[start] != s[i]:
                    set_substring.discard(s[start])
                    start += 1
                start += 1
            else:
                set_substring.add(s[i])
            i += 1
        res = res if res > i - start else i - start
        return res
