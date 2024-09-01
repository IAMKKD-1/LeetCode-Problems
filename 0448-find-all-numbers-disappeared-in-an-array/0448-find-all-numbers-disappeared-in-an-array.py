class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # d = set(nums)
        # a = []
        # for i in range(1, len(nums)+1):
        #     if i not in d:
        #         a.append(i)
        # return a

        ans = []
        seen = [False] * (len(nums)+1)
        for c in nums:
            seen[c] = True
        
        for i in range(1, len(nums)+1):
            if not seen[i]:
                ans.append(i)
        return ans