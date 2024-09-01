class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = set(nums)
        a = []
        for i in range(1, len(nums)+1):
            if i not in d:
                a.append(i)
        return a