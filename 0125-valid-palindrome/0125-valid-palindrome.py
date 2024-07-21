class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for i in s:
            if i.isalnum():
                arr.append(i.lower())
        start, end = 0, len(arr) -1
        while(start <= end):
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True