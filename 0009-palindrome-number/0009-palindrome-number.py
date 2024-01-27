class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            checker = 0
            num = x
            while num!=0:
                last = num%10
                checker = checker*10 + last
                num = num // 10
            if checker == x:
                return True
            else:
                return False