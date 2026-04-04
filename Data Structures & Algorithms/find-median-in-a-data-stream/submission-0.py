class MedianFinder:
    # ans = []
    def __init__(self):
        self.ans = []

    def addNum(self, num: int) -> None:
        self.ans.append(num)
        return None

    def findMedian(self) -> float:
        self.ans = sorted(self.ans)
        n = len(self.ans)
        if (n%2 == 1):
            return self.ans[n//2]
        else:
            # print(n//2)
            return (self.ans[n//2-1] + self.ans[(n//2)])/2
        