class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Convert to adjacency graph (undirected)
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Min-heap: (negative probability, node)
        min_heap = [(-1, start_node)]
        shortest_paths = set()  # Tracks visited nodes

        while min_heap:
            prob, cur = heapq.heappop(min_heap)
            shortest_paths.add(cur)

            # If we reach the end node, return the probability
            if cur == end_node:
                return -prob

            # Explore neighbors
            for neigh, edgeProb in graph[cur]:
                if neigh not in shortest_paths:
                    heapq.heappush(min_heap, (prob * edgeProb, neigh))

        # If the end node is unreachable, return 0
        return 0.0