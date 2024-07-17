class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        ans = []
        for i in candies:
            if i+extraCandies >= maxCandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans


