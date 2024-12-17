class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low = 0
        high = n - 1
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                high = mid - 1
            else:
                low = mid + 1
        return ans