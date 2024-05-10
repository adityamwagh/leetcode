                fracs.append(pair)

        fracs.sort(key=lambda x: x[0])  # Sort by fraction value

        # Create a min-heap based on fraction value
        heap = [(x[0], x[1], x[2]) for x in fracs]
        heapq.heapify(heap)

        # Pop the kth smallest fraction from the heap
        for _ in range(k - 1):
            heapq.heappop(heap)
[
