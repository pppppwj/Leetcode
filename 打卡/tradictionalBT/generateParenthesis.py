class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def aux(s, l, r):
            if l == 0:
                for i in s:
                    res.append(i + r * ")")
            else:
                if l > 0:
                    aux([ss + "(" for ss in s], l - 1, r + 1)
                if r > 0:
                    aux([ss + ")" for ss in s], l, r - 1)

        aux([""], n, 0)
        return res
