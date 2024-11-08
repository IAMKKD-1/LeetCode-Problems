class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = ''
        for i, j in d.items():
            if j == 1:
                c = i
                break
        if c:
            for i in range(len(s)):
                if s[i] == c:
                    return i
            
        return -1