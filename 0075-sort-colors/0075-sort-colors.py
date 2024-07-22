class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end, mid = 0, len(nums)-1, 0
        while mid <= end:
            if nums[mid]==0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 2: 
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
            else:
                mid += 1
            
        # idx = 0
        # while idx < len(nums):
        #     if nums[idx] == 0:
        #         nums
            
        
        

