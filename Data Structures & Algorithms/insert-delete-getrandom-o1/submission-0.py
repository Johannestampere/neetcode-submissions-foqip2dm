class RandomizedSet:

    def __init__(self):
        self.values = []     # idx -> value
        self.indices = {}    # value -> idx 

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        new_index = len(self.values)
        self.values.append(val)
        self.indices[val] = new_index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        idx_of_val = self.indices[val]
        idx_of_last_item = len(self.values) - 1
        val_of_last_item = self.values[idx_of_last_item]
        
        self.values[idx_of_val] = val_of_last_item
        self.values.pop(idx_of_last_item)

        self.indices[val_of_last_item] = idx_of_val
        self.indices.pop(val)

        return True

    def getRandom(self) -> int:
        random_index = random.randrange(len(self.values))
        return self.values[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()