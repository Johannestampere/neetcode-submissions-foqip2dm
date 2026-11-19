class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = [] #

        for p in s:
            if stack and p in h:
                if stack[-1] == h[p]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(p)
        
        if len(stack) == 0:
            return True

        return False