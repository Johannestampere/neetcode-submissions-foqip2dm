class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        curMin = [0] * (len(nums) + 1)
        curMax = [0] * (len(nums) + 1)
        curMin[0], curMax[0] = nums[0], nums[0]

        for i in range(1, len(nums)):

            curMax[i] = max(nums[i], curMax[i-1] * nums[i], curMin[i-1] * nums[i])
            curMin[i] = min(nums[i], curMax[i-1] * nums[i], curMin[i-1] * nums[i])    
            
        return max(curMax)
                