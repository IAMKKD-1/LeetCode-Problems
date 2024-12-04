class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans, prev = [], -1
        for w, b in zip(words, groups):
            if b != prev:
                prev = b
                ans.append(w)
        return ans   