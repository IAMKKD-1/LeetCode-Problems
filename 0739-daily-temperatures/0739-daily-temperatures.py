class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        stack = []

        for i, t in enumerate(temp):
            while stack and t > temp[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
