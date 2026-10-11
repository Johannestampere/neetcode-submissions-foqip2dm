class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda interval : interval[0])
        res = [] # stack

        for i in intervals:
            if not res:
                res.append(i)
                continue
            
            if res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)

        return res


