class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        prev = 2
        prevprev = 1

        for i in range(3, n + 1):
            tmp = prev + prevprev
            prevprev = prev
            prev = tmp
        
        return prev