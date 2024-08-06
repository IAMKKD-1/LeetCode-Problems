class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        li = sorted(d.items(), key=lambda x:x[1], reverse=True)
        print(li)
        final = []
        for i in range(k):
            final.append(li[i][0])
        print(final)
        return final