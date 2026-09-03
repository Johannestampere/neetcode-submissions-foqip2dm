from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in counts.items():
            buckets[v].append(key)

        res = []

        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res




