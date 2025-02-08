from sortedcontainers import SortedDict, SortedSet
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.store = SortedDict()  # Maps index -> number
        self.number_map = defaultdict(SortedSet)  # Maps number -> sorted set of indices

    def change(self, index: int, number: int) -> None:
        if index in self.store:
            old_number = self.store[index]
            self.number_map[old_number].discard(index)  # Remove old index from number map
            if not self.number_map[old_number]:  # Cleanup if empty
                del self.number_map[old_number]

        self.store[index] = number
        self.number_map[number].add(index)  # Insert new index in sorted set

    def find(self, number: int) -> int:
        if number in self.number_map and self.number_map[number]:
            return next(iter(self.number_map[number]))  # Get the smallest index
        return -1  # Return -1 if number is not found
