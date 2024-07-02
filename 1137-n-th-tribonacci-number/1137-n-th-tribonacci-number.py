class Solution:
    def tribonacci(self, n: int) -> int:
        li = [0,1,1]
        if n < 3:
            return li[n]
        else:
            for i in range(3, n+1):
                li.append(li[-1] + li[-2] + li[-3])
        return li[n]