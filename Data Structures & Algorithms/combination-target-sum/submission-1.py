class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, curNums, total):

            if i >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(curNums[:])
                return
            
            curNums.append(nums[i])
            backtrack(i, curNums, total + nums[i])

            curNums.pop()
            backtrack(i + 1, curNums, total)

        backtrack(0, [], 0)
        return res
        
            