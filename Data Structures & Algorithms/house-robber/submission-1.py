class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0   # if we rob n, we must rob rob1
                            # if we don't rob n, we must rob rob2

        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2