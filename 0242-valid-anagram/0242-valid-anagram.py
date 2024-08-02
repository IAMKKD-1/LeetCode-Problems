class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for i in s:
            if i in sd:
                sd[i] += 1
            else:
                sd[i] = 1

        for j in t:
            if j in sd:
                sd[j] -= 1

        for i in sd.values():
            if i != 0:
                return False
                
        return True 
            