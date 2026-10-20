class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L, R = 0, len(heights) - 1
        maxArea = 0

        while R > 0 and L < len(heights):

            maxArea = max((R - L) * min(heights[L], heights[R]), maxArea)

            if heights[L] < heights[R]:
                L += 1
            
            else:
                R -= 1
        
        return maxArea
            