from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, freq in freqs.items():
            buckets[freq].append(n)

        res = []
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res






