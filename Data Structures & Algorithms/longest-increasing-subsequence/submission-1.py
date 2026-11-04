class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [] # tails[k] -> the smallest possible ending val
                    # of a strictly increasing subseq of len k + 1 seen 
                    # so far
        
        for x in nums:
            L, R = 0, len(tails)

            # find first idx where tails[i] >= x
            while L < R:
                mid = (L + R) // 2

                if tails[mid] < x:
                    L = mid + 1
                else:
                    R = mid
            
            if L == len(tails):
                tails.append(x)
            else:
                tails[L] = x

        return len(tails)