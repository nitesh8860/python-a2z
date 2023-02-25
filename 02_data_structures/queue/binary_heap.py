class BinHeap:
    def __init__(self) -> None:
        self.heapList = [0]
        self.curSize = 0
    
    def getMin(self):
        return self.heapList[1]
    
    def percDown(self, i):
        while i * 2 <= self.curSize
        minn = self.minChild

    def buildHeap(self, alist):
        i = len(alist)//2
        self.curSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
