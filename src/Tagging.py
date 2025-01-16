# from collections import heapq
import heapq
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class FileCollection:
    def __init__(self, id):
        self.id = id
        self.files = []
        self.size = 0

    def add(self, file: File):
        self.files.append(file)
        self.size += file.size

class Tagging:
    def __init__(self):
        self.collections: dict[str, FileCollection] = {}
        self.size = 0

    def size(self) -> int:
        return self.size

    def add_file(self, collection: str, file: File):
        if not collection:
            collection = "default"
        if collection not in self.collections:
            self.collections[collection] = FileCollection(collection)
        self.collections[collection].add(file)
        self.size += file.size

    def top_n(self, n: int) -> list[str]:
        heap: list[(int, FileCollection)] = []
        for name in self.collections:
            collection = self.collections[name]
            heapq.heappush(heap, (collection.size, collection))
            # Keep it n * log(k)
            if len(heap) > n:
                heapq.heappop(heap)
        ans = []
        for (size, coll) in heap:
            ans.append(coll.id)
        return ans