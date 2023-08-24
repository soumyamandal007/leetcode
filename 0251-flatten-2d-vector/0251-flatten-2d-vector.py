class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = []
        for in_list in vec:
            for element in in_list:
                self.v.append(element)
        self.pos = -1

    def next(self) -> int:
        self.pos += 1
        return self.v[self.pos]

    def hasNext(self) -> bool:
        return self.pos < len(self.v) - 1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()