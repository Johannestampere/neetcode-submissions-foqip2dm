class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = [False for i in range(len(nums))]
        l = len(nums)
        def backtrack(n):
            if n == l:
                res.append(curr[:])

            for i in range(l):
                if not seen[i]:
                    seen[i] = True
                    curr.append(nums[i])
                    backtrack(n + 1)
                    seen[i] = False
                    curr.pop()
                    
        backtrack(0)
        return res
    


            