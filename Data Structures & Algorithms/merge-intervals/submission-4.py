class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda interval : interval[0])

        stack = []


        # (1,4) 
        for interval in intervals:

            if not stack:
                stack.append(interval)
                continue
            
            if stack[-1][1] >= interval[0]:
                stack[-1] = [stack[-1][0], max(stack[-1][1], interval[1])]

            else:
                stack.append(interval)

        return stack