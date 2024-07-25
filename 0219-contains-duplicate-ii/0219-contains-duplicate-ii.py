class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window = set()
        # i, j = 0, 0
        # while j < len(nums):
        #     if j-i > k:
        #         window.remove(nums[i])
        #         i+=1
        #     if nums[j] in window:
        #         return True
        #     window.add(nums[j])
        #     j+=1
        # return False
            
        sett = {}
        for i, j in enumerate(nums):
            if j in sett and i - sett[j] <= k:
                return True
            sett[j] = i
        return False