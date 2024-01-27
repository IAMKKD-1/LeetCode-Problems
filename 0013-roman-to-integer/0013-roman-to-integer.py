class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and data[s[i]] < data[s[i+1]]:
                total -= data[s[i]]
            else:
                total += data[s[i]]
        return total