class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.fib(n-1) + self.fib(n-2)

        #Alternate solution
        li = [0, 1]
        if n < 2:
            return li[n]
        else:
            for i in range(2, n+1):
                li.append(li[-1] + li[-2])
        
        return li[-1]