class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Larr = 1, 1, 2, 8
        # Rarr = 48, 24, 6, 1

        Larr = [0] * len(nums)
        Larr[0] = 1
        Ltracker = 1
        for i in range(1, len(nums)):
            Larr[i] = nums[i - 1] * Ltracker
            Ltracker = Larr[i]
        
        Rarr = [0] * len(nums)
        Rarr[-1] = 1
        Rtracker = 1
        for i in range(len(nums)-2, -1, -1):
            Rarr[i] = nums[i + 1] * Rtracker
            Rtracker = Rarr[i]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = Rarr[i] * Larr[i]

        return res