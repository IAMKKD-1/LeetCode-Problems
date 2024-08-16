class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0; t = 0
        for i in bills:
            if i == 5:
                f+=1
            elif i == 10 and f >= 1:
                t+=1
                f-=1
            elif i == 20 and f>=1 and t>=1:
                f-=1
                t-=1
            elif i == 20 and f>=3:
                f-=3
            else:
                print(f, t)
                return False
        return True