class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L, R = 0, len(nums) - 1

        while L < R:

            mid = (L + R) // 2

            if nums[R] > nums[mid]:
                R = mid
            
            else:
                L = mid + 1

        return nums[L]