class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        pre = 1
        for i in range(len(nums)):
            out.append(pre)
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post
            post *= nums[i]
        
        return out