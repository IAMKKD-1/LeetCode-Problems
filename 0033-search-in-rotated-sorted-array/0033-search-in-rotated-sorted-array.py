class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     mid = (i+j)//2
        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[i] <= nums[m]:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
                

