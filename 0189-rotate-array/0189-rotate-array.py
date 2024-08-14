class Solution:
    def reverse(self, arr, l, h):
        while l<h:
            arr[l], arr[h] = arr[h], arr[l]
            l+=1
            h-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
            
        