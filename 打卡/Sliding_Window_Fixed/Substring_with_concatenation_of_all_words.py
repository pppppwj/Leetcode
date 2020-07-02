from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        words_counter = {}
        for i in range(len(words)):
            if words[i] in words_counter:
                words_counter[words[i]] += 1
            else:
                words_counter[words[i]] = 1
        words_counter_copy = words_counter.copy()
        len_of_singleWord = len(words[0])
        res = []
        for j in range(len_of_singleWord):
            words_counter = words_counter_copy.copy()
            i = start = j
            while i <= (len(s) - len_of_singleWord):
                if s[i : i + len_of_singleWord] in words_counter:
                    if words_counter[s[i : i + len_of_singleWord]] > 0:
                        words_counter[s[i : i + len_of_singleWord]] -= 1

                    else:
                        while (
                            s[start : start + len_of_singleWord]
                            != s[i : i + len_of_singleWord]
                        ):
                            words_counter[s[start : start + len_of_singleWord]] += 1
                            start += len_of_singleWord
                        start += len_of_singleWord
                    i += len_of_singleWord
                else:
                    start = i + len_of_singleWord
                    i = start
                    words_counter = words_counter_copy.copy()

                if i - start == len_of_singleWord * len(words):
                    res.append(start)

        return res
