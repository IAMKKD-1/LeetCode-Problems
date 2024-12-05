class Solution:
    def findLHS(self, A):
        count = collections.Counter(A)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans 