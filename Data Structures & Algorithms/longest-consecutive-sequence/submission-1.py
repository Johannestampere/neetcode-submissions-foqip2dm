class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums) 
        longest = 0

        for n in nums:
            if n - 1 not in s:
                cur = n
                l = 1

                while cur + 1 in s:
                    l += 1
                    cur += 1
                
                longest = max(longest, l)
        
        return longest
