class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_map = defaultdict(list) # node -> [(weight_to_next, next)]
        for src, target, weight in times:
            edge_map[src].append((weight, target))

        minHeap = [(0, k)]
        visited = set()
        totalTime = 0

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)

            if node1 in visited:
                continue

            visited.add(node1)

            totalTime = max(totalTime, time1)

            for weight, target in edge_map[node1]:
                if target not in visited:
                    heapq.heappush(minHeap, (time1 + weight, target))
        
        if len(visited) != n:
            return -1

        return totalTime
        

