class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -=1
        if n<=0:
            return True
        return False

        # count = 0
        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 1:
        #         if n == 1:
        #             return False
        #         else:
        #             return True
        #     else:
        #         return True
                
        # for i in range(0, len(flowerbed)):
        #     print(i)
        #     if i == 0 and flowerbed[i] + flowerbed[i+1] == 0:
        #         count += 1
        #         flowerbed[i] = 1  
        #     elif i == len(flowerbed) - 1:
        #         if flowerbed[i] + flowerbed[i-1] == 0:
        #             count += 1
        #             flowerbed[i] = 1
        #     elif flowerbed[i] + flowerbed[i+1] + flowerbed[i-1] == 0:
        #         count += 1
        #         flowerbed[i] = 1
        # if count >= n:
        #     return True
        # return False