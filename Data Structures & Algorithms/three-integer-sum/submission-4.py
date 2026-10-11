class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        for i in range(len(nums)):

            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                s = nums[L] + nums[R] + nums[i]
                if s == 0:
                    res.append([nums[L], nums[R], nums[i]])
                    R -= 1
                    L += 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

                elif s < 0:
                    L += 1
                else:
                    R -= 1

        return res
             