class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        counter = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                counter += 1
        
        if nums[n-1] > nums[0]:
            counter+=1
        
        return counter <= 1
        
