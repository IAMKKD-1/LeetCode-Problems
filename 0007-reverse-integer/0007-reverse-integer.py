class Solution:
    def reverse(self, x: int) -> int:
        pos = 1
        if x<0:
            pos=0
            x *= -1
        n = list(str(x))
        i = 0
        j = len(n)-1
        while i<=j:
            n[i], n[j] = n[j], n[i]
            i+=1
            j-=1
        ans = int(''.join(n))
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        if pos == 1:
            return ans
        return -1 * ans