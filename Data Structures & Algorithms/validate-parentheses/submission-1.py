class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for p in s:
            if p in h:
                if stack and stack[-1] == h[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if len(stack) == 0:
            return True
        else:
            return False