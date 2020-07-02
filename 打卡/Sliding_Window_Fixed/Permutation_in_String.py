class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = {}
        for i in range(len(s1)):
            if s1[i] in s1_counter:
                s1_counter[s1[i]] += 1
            else:
                s1_counter[s1[i]] = 1

        s1_counter_copy = s1_counter.copy()
        start = i = 0

        while i < len(s2):
            if s2[i] in s1_counter:
                if s1_counter[s2[i]] > 0:
                    s1_counter[s2[i]] -= 1
                else:
                    while s2[start] != s2[i]:
                        s1_counter[s2[start]] += 1
                        start += 1
                    start += 1
                i += 1
            else:
                s1_counter = s1_counter_copy.copy()
                start = i + 1
                i += 1
            if i - start == len(s1):
                return True
        return False
