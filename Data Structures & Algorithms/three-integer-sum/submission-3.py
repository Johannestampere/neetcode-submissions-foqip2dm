class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nlogn sort
        nums.sort()

        # -5 -3 -1 0 1 2 2 3 6

        res = []

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                s = nums[L] + nums[R] + nums[i]

                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    res.append([nums[R], nums[L], nums[i]])
                    tmpLVal = nums[L]
                    tmpRVal = nums[R]

                    while L < R and nums[L] == tmpLVal:
                        L += 1
                    while R > L and nums[R] == tmpRVal:
                        R -= 1

        return res

