class Solution:
    # def fact(self, num: int) -> int:
    #     ans = 1
    #     for i in range(1, num+1):
    #         ans *= i
    #     return ans

    def numIdenticalPairs(self, nums: List[int]) -> int:
        # d = {}
        # ans = 0
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        
        # for i in d.values():
        #     if i == 1:
        #         continue
        #     else:
        #         ans += self.fact(i)//(2*(self.fact(i-2)))
        # return ans


        # count = Counter(nums)
        # ans = 0
        # for i in count.values():
        #     ans += i * (i-1) // 2
        # return ans


        d = {}
        ans = 0
        for i in nums:
            if i in d:
                ans += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return ans