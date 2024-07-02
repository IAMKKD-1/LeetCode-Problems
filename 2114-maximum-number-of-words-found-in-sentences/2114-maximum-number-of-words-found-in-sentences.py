class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxc = 0
        for i in sentences:
            length = len(i.split(' '))
            if length > maxc:
                maxc = length
        return maxc