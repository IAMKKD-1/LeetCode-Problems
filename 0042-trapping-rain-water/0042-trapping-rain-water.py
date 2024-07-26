class Solution:
    def trap(self, height: List[int]) -> int:
        ml = [0]*len(height)
        mr = [0]*len(height)
        maxl=0
        maxr=0
        i, j = 0, len(height) - 1
        while i<len(height):
            ml[i] = maxl
            mr[j] = maxr
            if height[i] > maxl:
                maxl = height[i]        
            if height[j] > maxr:
                maxr = height[j]   
            i+=1
            j-=1
        ans = []
        for i in range(len(ml)):
            mini = min(ml[i], mr[i])
            if mini - height[i] <= 0:
                ans.append(0)
            else:
                ans.append(mini - height[i])
        return sum(ans)
