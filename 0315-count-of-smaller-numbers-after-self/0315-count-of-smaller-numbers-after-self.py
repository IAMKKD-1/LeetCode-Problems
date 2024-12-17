class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def merge_sort(arr, counts):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid], counts)
            right = merge_sort(arr[mid:], counts)
            merged = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    merged.append(left[i])
                    counts[left[i][0]] += len(right) - j
                    i+=1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
              merged.append(left[i])
              i+=1

            while j < len(right):
              merged.append(right[j])
              j+=1
            return merged

        indexed_nums = [(i, num) for i, num in enumerate(nums)]
        counts = [0] * len(nums)
        merge_sort(indexed_nums, counts)
        return counts