class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        # find min index
        while l < r:
            m = (r + l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        min_index = l

        # choose correct portion
        if min_index == 0:
            l, r = 0, n - 1
        elif target >= nums[min_index] and target <= nums[n - 1]:
            l, r = min_index, n - 1
        else:
            l, r = 0, min_index - 1

        
        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1