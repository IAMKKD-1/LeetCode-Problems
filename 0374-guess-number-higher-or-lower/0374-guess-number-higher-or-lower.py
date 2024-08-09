# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        while l <= n:
            m = (l+n)//2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                n = m-1
            else:
                l = m+1
            