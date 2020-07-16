# using dp
def isMatch(text: str, pattern: str) -> bool:
    memo = {}  # empty dict to store whether test[i:] match pattern[j:]

    # if test[i:] match pattern[j:] return True else False
    # dp logic
    # if test[i:] match pattern[j:]
    # x + pattern[j:] match x + test[i:]
    # x* + pattern[j:] match test[k:i] + test[i:]
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                match = i < len(text) and pattern[j] in {".", text[i]}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    ans = dp(i, j + 2) or match and dp(i + 1, j)
                else:
                    ans = match and dp(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)



