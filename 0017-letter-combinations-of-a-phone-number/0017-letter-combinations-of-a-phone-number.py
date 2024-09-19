class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        
        def backtrack(idx, final):
            if len(final) == len(digits):
                res.append(final)
                return 

            for i in a[digits[idx]]:
                backtrack(idx+1, final+i)
        
        if digits:
            backtrack(0, '')
        return res
                
