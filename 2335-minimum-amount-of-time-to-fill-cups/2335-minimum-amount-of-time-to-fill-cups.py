class Solution:
    def fillCups(self, A: List[int]) -> int:
        return max(max(A), (sum(A) + 1) // 2)
