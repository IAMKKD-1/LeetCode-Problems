class Solution:
    def reverseString(self, arr: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()

        start = 0
        end = len(arr) - 1
        while(start < end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr