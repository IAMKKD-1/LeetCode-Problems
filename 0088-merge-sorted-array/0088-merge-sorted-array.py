class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = m+n-1
        while k >= 0:
            if i == -1:
                nums1[k] = nums2[j]
                j-=1
            elif j == -1:
                pass 
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j-=1    
            else:
                nums1[k] = nums1[i]
                i-=1            
            k-=1


        # i, j = 0, 0
        # while j != len(nums2):
        #     print(i, j)
        #     if nums2[j]<=nums1[i]:
        #         nums1.insert(i, nums2[j])
        #         j+=1
        #     elif i >= m and nums1[i] == 0:
        #         nums1[i] = nums2[j]
        #         j+=1
        #     else:
        #         i+=1
        # for k in range(len(nums1)-1, -1, -1):
        #     if nums1[k] == 0:
        #         nums1.pop(k)
        #     else:
        #         break
            