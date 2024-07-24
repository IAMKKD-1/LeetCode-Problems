class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in d:
                return [i, d[val]]
            else:
                d[nums[i]] = i
        















