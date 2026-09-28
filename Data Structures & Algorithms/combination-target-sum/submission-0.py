class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = [] # pointer first element []

        def backtrack(i, s):
            # base case
            if s == target:
                res.append(curr[:])
                return
            if s > target:
                return
            if i == len(nums):
                return
            #  case 1: append the number
            curr.append(nums[i]) # [2,5,6]
            backtrack(i, s + nums[i])
            curr.pop()
            # case 2: ignore the number

            backtrack(i + 1, s)



        backtrack(0, 0)
        return res