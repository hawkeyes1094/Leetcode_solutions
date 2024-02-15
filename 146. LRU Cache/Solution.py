class LRUCache:
    def __init__(self, capacity: int):
        self.__Cache = {}
        self.__CacheCapacity = 0
        self.__TotalCapacity = capacity
        self.__LRU = []

    def _updateLRU(self, key: int) -> None:
        self.__LRU.remove(key)
        self.__LRU.append(key)

    def _addLRU(self, key: int) -> None:
        self.__LRU.append(key)

    def _delLRU(self) -> int:
        return self.__LRU.pop(0)

    def get(self, key: int) -> int:
        retval = self.__Cache.get(key)
        if retval is not None:
            self._updateLRU(key)
            return retval
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.__Cache:
            self.__Cache[key] = value
            self._updateLRU(key)
        else:
            if self.__CacheCapacity == self.__TotalCapacity:
                toDelete = self._delLRU()          
                del self.__Cache[toDelete]
                self.__Cache[key] = value
                self._addLRU(key)
            else:
                self.__Cache[key] = value
                self._addLRU(key)
                self.__CacheCapacity = self.__CacheCapacity + 1
        
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)