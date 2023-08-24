class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.vals_ind = {}

    def insert(self, val: int) -> bool:
        if val in self.vals_ind:
            return False
        self.vals_ind[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals_ind:
            return False
        index = self.vals_ind[val]
        last_val = self.vals[-1]
        self.vals[index] = last_val
        self.vals_ind[last_val] = index
        self.vals.pop()
        del self.vals_ind[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()