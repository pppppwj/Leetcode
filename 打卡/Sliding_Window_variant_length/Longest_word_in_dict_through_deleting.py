from collections import defaultdict
from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # chars lists
        letters_positions = defaultdict(list)

        # init letters_positions
        for i in range(len(s)):
            letters_positions[s[i]].append(i)
        for word in sorted(d, key=lambda w: (-len(w), w)):
            p = -1
            nextWord = False
            for letter in word:

                if letter not in letters_positions:
                    nextWord = True
                    break
                else:
                    pnt = 0
                    while (
                        pnt < len(letters_positions[letter])
                        and p >= letters_positions[letter][pnt]
                    ):
                        pnt += 1
                    if pnt >= len(letters_positions[letter]):
                        nextWord = True
                        break
                    else:
                        p = letters_positions[letter][pnt]

            if not nextWord:
                return word
        return ""

    def findLongestWord2(self, s: str, d: List[str]) -> str:
        s_dict = {s[i]:i for i in range(len(s)-1,-1,-1)}
        occurence = defaultdict(list)
        for i,c in enumerate(s):
            for _ in range(i-len(occurence[c])): occurence[c].append(i)
        for l in occurence.values():
            for _ in range(len(s)-len(l)): l.append(-1)

        print(occurence)

if __name__ == "__main__":
    sol = Solution()
    s = "abpcplea"
    sol.findLongestWord2(s,[])