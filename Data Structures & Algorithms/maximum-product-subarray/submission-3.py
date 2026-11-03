class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMin = nums[0]
        curMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            prevMin = curMin
            prevMax = curMax

            curMax = max(nums[i], prevMin * nums[i], prevMax * nums[i])
            curMin = min(nums[i], prevMin * nums[i], prevMax * nums[i])

            res = max(curMax, res)

        return res