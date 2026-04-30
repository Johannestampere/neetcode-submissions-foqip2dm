from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = defaultdict(int)

        for n in nums:
            h[n] += 1
        
        # 7 : 2
        buckets = [[] for _ in range(len(nums) + 1)]

        # buckets = [[], [], []]
        for key in h:
            buckets[h[key]].append(key)
        
        # buckets = [[], [], [7]]

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

