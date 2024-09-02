class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums = list(set(nums))
        nums.sort()
        
        maxx = 1
        curr = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                curr += 1
                maxx = max(curr, maxx)
            else:
                curr = 1
        return maxx
