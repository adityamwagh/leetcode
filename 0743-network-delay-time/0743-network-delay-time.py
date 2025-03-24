class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # Convert graph to adjacency list
        graph = {}
        for i in range(1, n+1):
            graph[i] = list()

        for u, v, w in times:
            graph[u].append((v, w))

        # Time to reach each node
        times = {}
        min_heap = [(0, k)]

        while min_heap:

            time_to_reach_node, node = heapq.heappop(min_heap)

            # if node exists in time, it's guaranteed to be 
            # minimum since we use a min heap to find least 
            # weighted path, so skip checking neighbors
            if node in times:
                continue
            times[node] = time_to_reach_node

            for neigh, weight in graph[node]:
                if neigh not in times:
                    heapq.heappush(min_heap, (weight + time_to_reach_node, neigh))
        
        # Check if all nodes received the signal
        if len(times) != n:
            return -1
        
        # Return the maximum time (how long it takes for all nodes to receive)
        return max(times.values())
