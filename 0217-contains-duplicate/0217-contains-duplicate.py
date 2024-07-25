class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sol 1 O(n logn)

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # Sol 2 O(n)
        # sett = set()
        # for i in nums:
        #     if i in sett:
        #         return True
        #     else:
        #         sett.add(i)
        # return False

        # Sol 3 O(n)
        # dictt = {}
        # for i in nums:
        #     if i in dictt:
        #         return True
        #     else:
        #         dictt[i] = 1
        # return False    
        
        if len(set(nums)) == len(nums):
            return False
        return True