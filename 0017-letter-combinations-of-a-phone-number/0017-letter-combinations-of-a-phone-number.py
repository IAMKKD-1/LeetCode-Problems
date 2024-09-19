class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
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

            for c in mapping[digits[idx]]:
                backtrack(idx + 1, final + c)

        if digits:
            backtrack(0, "")

        return res
