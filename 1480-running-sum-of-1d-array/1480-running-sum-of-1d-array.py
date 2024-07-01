class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     ans.append(sum(nums[:i+1]))
        # return ans

        ans = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            ans.append(ans[i-1] + nums[i])
        return ans