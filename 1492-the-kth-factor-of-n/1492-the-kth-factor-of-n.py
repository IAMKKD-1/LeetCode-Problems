class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        li = []
        for i in range(1,n+1):
            if n%i == 0:
                li.append(i)
                if len(li) == k:
                    return li[k-1]
                print(li)
        return -1