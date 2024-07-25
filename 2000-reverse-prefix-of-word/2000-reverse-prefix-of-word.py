class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j = -1
        for i in range(len(word)):
            if word[i] == ch:
                j = i
                break
        if j != -1:
            return word[:j+1][::-1] + word[j+1:]
        return word 
        

                 