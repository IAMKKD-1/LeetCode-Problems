class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # j = 0
        # i = 0
        # while i < len(haystack):
        #     if haystack
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1