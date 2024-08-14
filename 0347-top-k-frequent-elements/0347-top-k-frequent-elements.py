class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        li = [[] for i in range(len(nums)+1)]
        for i in d:
            li[d[i]].append(i)
        final = []
        for i in range(len(li)-1, -1, -1):
            # if li[i]:
            #     final.extend(li[i])
            #     if len(final) == k:
            #         return final
            # OR
            for i in li[i]:
                final.append(i)
                if len(final) == k:
                    return final

        # li = sorted(d.items(), key=lambda x:x[1], reverse=True)
        
        # final = []
        # for i in range(k):
        #     final.append(li[i][0])
        # return final