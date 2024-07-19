class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1,-1, -1):
            if s[i] != ' ':
                ans += 1
            elif s[i] == ' ' and ans != 0:
                return ans         
        return ans