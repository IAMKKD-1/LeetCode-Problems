class Solution:
    def removeStars(self, s: str) -> str:
        new = []
        for i in range(len(s)):
            if s[i] == '*':
                new.pop()
            else:
                new.append(s[i])
        return ''.join(new)