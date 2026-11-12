class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap) # minHeap always stores K largest so far.
                # so we pop the min when size is too large -> logn

        return heapq.heappop(minHeap)

