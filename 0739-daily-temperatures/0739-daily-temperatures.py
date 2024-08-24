class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        t = [0]*len(temp)

        for i, j in enumerate(temp):
            while stack and j > stack[-1][0]:
                t[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()
            stack.append((j, i))
        return t
        






















        # ans = [0]*len(temp)
        # stack = []
        # for i, t in enumerate(temp):
        #     while stack and t > temp[stack[-1]]:
        #         idx = stack.pop()
        #         ans[idx] = i - idx
        #     stack.append(i)
        # return ans