class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        high = 0
        ss = set()
        while j < len(s):
            if s[j] not in ss:
                ss.add(s[j])
                high = max(high, len(ss))
                j+=1
            else:
                ss.remove(s[i])
                i+=1
        return high

