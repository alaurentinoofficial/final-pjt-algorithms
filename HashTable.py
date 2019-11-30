class HashTable:

    def __init__(self, size = 3000):
        self.__table = [[] for _ in range(size)]
    
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        return self.search(key)
    
    def __contains__(self, key):
        return self.search(key) != None
    
    def hashing_fn(self, key):
        return hash(key) % len(self.__table)

    def insert(self, key, value):
        hash_key = self.hashing_fn(key)
        self.__table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self.hashing_fn(key)

        if hash_key < len(self.__table):
            for item in self.__table[hash_key]:
                if item[0] == key:
                    return item[1]
    
    def pop(self, key):
        hash_key = self.hashing_fn(key)

        if hash_key < len(self.__table):
            for i, item in enumerate(self.__table[hash_key]):
                if item[0] == key:
                    item.pop(i)
                    return

if __name__ == "__main__":
    map_table = HashTable()

    map_table.insert("oi", "sim")
    map_table.insert("teste", "mais ou menos")

    print(map_table.search("oi"))
    print(map_table.search("nao"))
    print(map_table.search("Teste"))
    print(map_table.search("teste"))