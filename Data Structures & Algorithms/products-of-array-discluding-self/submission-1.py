class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums
        
        # nums = [2, 3, 4, 5]
        # output = [60, 40, 30, 24]
        # [1, 2, 6, 24]
        # [1, 1, 5, 1]
        # m = 5

        #rightpass
        left_arr = [1]
        multiplier = 1
        for i in range(len(nums)):
            left_arr.append(multiplier * nums[i])
            multiplier *= nums[i]
        
        #leftpass
        right_arr = [1 for _ in range(len(nums))]
        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            right_arr[i] = multiplier
            multiplier *= nums[i]

        for i in range(len(nums)):
            right_arr[i] *= left_arr[i]

        return right_arr


