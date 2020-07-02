from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_counter = {}
        for i in range(len(p)):
            if p[i] in p_counter:
                p_counter[p[i]] += 1
            else:
                p_counter[p[i]] = 1
        p_counter_copy = p_counter.copy()
        start = i = 0
        while i < len(s):
            if s[i] in p_counter:
                if p_counter[s[i]] > 0:
                    p_counter[s[i]] -= 1
                else:
                    while s[start] != s[i]:
                        p_counter[s[start]] += 1
                        start += 1
                    start += 1
                i += 1
            else:
                p_counter = p_counter_copy.copy()
                start = i + 1
                i += 1
            if i - start == len(p):
                res.append(start)
        return res

