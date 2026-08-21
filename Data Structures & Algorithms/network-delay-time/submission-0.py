class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list) # source -> [[target, time to target]]

        for source, target, time in times:
            edges[source].append((target, time))

        minHeap = [(0, k)] # tracks (time, target)
        visited_nodes = set()
        t = 0

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if node1 in visited_nodes:
                continue
            visited_nodes.add(node1)
            t = max(time1, t)

            for node2, time2 in edges[node1]:
                if node2 not in visited_nodes:
                    heapq.heappush(minHeap, (time1 + time2, node2))
        
        if len(visited_nodes) != n:
            return -1
        return t

