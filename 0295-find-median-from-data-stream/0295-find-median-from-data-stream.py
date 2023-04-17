class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap.sort()
        length = len(self.heap)
        print(length//2-1,(length//2) )
        if length % 2 == 0:
            f = self.heap[(length)//2-1]
            s = self.heap[(length//2)]
            return round((f+s)/2,5)
        else:
            return round((self.heap[(length+1)//2-1]),5)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()