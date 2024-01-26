class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for curridx in range(len(nums)):
            diff = target - nums[curridx]
            if diff in h:
                return [h[diff], curridx]
            else:
                h[nums[curridx]] = curridx

    