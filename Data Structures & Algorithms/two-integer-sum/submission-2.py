class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            if target - nums[i] not in h:
                h[nums[i]] = i
            else:
                return [min(i, h[target-nums[i]]), max(i, h[target-nums[i]])]