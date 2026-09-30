class Solution:
    def rob(self, nums: List[int]) -> int:

        r1, r2 = 0, 0 # r2 is the last house we robbed, r1 the one before that

        for n in nums:
            tmp = max(n + r1, r2)   
            r1 = r2
            r2 = tmp

        return r2   