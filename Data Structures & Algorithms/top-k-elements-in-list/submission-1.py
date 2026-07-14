from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums=[1,2,2,3,3,3]
        h = defaultdict(int)

        for n in nums:
            h[n] += 1
        # h = {1:1, 2:2, 3:3}
        buckets = [[] for _ in range(len(nums)+1)]
        # buckets = [[], [1], [2], [3], [], [], []]

        for n in h:
            buckets[h[n]].append(n)

        res = []

        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])

        return res

