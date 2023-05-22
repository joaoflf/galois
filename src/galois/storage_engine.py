import sortedcontainers


class StorageEngine:
    def __init__(self):
        self._memtable = sortedcontainers.SortedDict()

    def get(self, key):
        return self._memtable.get(key)

    def put(self, key, value):
        self._memtable[key] = value

    def delete(self, key):
        del self._memtable[key]
