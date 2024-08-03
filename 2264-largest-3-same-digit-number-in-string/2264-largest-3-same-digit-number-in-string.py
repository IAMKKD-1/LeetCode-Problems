class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        li = 0
        check = False
        while i < len(num) - 2:
            if num[i] == num[i+1] == num[i+2]:
                li = max(li, int(num[i]))
                check=True
            i+=1

        if check:
            return str(li)*3 
        return ""