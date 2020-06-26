# Time complexity : O(n). Index j will iterate n times.

# Space complexity (HashMap) : O(min(m, n)). Same as the previous approach.

# Space complexity (Table): O(m). m is the size of the charset.


def lengthOfLongestSubstring(s):
    start = -1
    res = 0
    alp = {}
    for i in range(len(s)):
        if s[i] in alp and alp[s[i]] > start:
            start = alp[s[i]]
        alp[s[i]] = i
        res = i - start if i - start > res else res
    return res
