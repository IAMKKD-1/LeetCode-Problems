class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = len(nums) - 1
        # while i >= 0:
        #     if nums[i] == val:
        #         nums.remove(nums[i])
        #     i-=1
        # return len(nums)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
