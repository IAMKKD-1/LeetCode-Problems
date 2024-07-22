class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # size = (len(nums) // 2 ) + 1
        # dictt = {}
        # if size == 1:
        #     return nums[0]
        # for i in nums:
        #     if i not in dictt:
        #         dictt[i] = 1
        #     elif dictt[i] == size or dictt[i] == size - 1 :
        #         return i
        #     else:
        #         dictt[i] += 1

        candidate = 0
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        
        
