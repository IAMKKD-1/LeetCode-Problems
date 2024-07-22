class Solution:
    def maxArea(self, height: List[int]) -> int:
        ll = len(height)
        l = 0
        h = ll - 1
        store = 0
        while l < h:
            mini = min(height[l], height[h])
            store = max(store, mini * (h-l))
            if height[l] < height[h]:
                l+=1
            # elif height[l] > height[h]:
            #     h-=1
            else:
                # l+=1
                h-=1
        return store