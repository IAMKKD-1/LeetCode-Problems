class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1) - 1
        s1 = sorted(s1)
        while j<len(s2):
            if sorted(s2[i:j+1]) == s1:
                return True
            i+=1
            j+=1
        return False
