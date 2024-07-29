class Solution:
    def convert(self, s: str, n: int) -> str:
        # Need Improvement
        if n == 1:
            return s
        d = {}
        for i in range(n):
            d[i] = ''
        n = n-1
        for i in range(len(s)):
            ct = n-abs(n-(i%(2*n)))
            d[ct] += s[i]
        final = ''
        for i in d.values():
            final += i
        return final

