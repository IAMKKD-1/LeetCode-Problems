class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and abs(ord(i) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

        # for i in range(len(s)):
        #     if stack:
        #         if s[i] == stack[-1]:
        #             stack.append(s[i])
        #         else:
        #             if stack[-1].lower() == s[i] or s[i].lower() == stack[-1]:
        #                 stack.pop()
        #             else:
        #                 stack.append(s[i]) 
        #     else:
        #         stack.append(s[i])
        # return ''.join(stack)