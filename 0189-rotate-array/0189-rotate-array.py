class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        i = 0
        while k != 0:
            nums.insert(i, nums[-k])
            nums.pop(-k)
            i+=1
            k-=1
            
        