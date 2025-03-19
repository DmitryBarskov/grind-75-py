from typing import List

import heapq

class MedianFinder:
    """
    >>> mf = MedianFinder()
    >>> mf.addNum(1)
    >>> mf.addNum(2)
    >>> mf.findMedian()
    1.5
    >>> mf.addNum(3)
    >>> mf.findMedian()
    2.0
    >>> mf.addNum(0)
    >>> mf.findMedian()
    1.5
    >>> mf.addNum(4)
    >>> mf.findMedian()
    2.0
    >>> mf.addNum(10) # 0 1 2 3 4 10
    >>> mf.findMedian()
    2.5
    >>> mf.addNum(12) # 0 1 2 3 4 10 12
    >>> mf.findMedian()
    3.0
    >>> mf.addNum(15) # 0 1 2 3 4 10 12 15
    >>> mf.findMedian()
    3.5
    >>> mf.addNum(20) # 0 1 2 3 4 10 12 15 20
    >>> mf.findMedian()
    4.0
    >>> mf.addNum(30) # 0 1 2 3 4 10 12 15 20 30
    >>> mf.findMedian()
    7.0

    >>> mf = MedianFinder()
    >>> (mf.addNum(6), mf.findMedian())[1]
    6.0
    >>> (mf.addNum(10), mf.findMedian())[1]
    8.0
    >>> (mf.addNum(2), mf.findMedian())[1] # 2 6 10
    6.0
    >>> (mf.addNum(6), mf.findMedian())[1]
    6.0
    >>> (mf.addNum(5), mf.findMedian())[1]
    6.0
    >>> (mf.addNum(0), mf.findMedian())[1]
    5.5
    >>> (mf.addNum(6), mf.findMedian())[1]
    6.0
    >>> (mf.addNum(3), mf.findMedian())[1]
    5.5
    >>> (mf.addNum(1), mf.findMedian())[1]
    5.0
    >>> (mf.addNum(0), mf.findMedian())[1]
    4.0
    >>> (mf.addNum(0), mf.findMedian())[1]
    3.0
    """

    def __init__(self):
        self._ltm: List[tuple[int, int]] = [] # max heap with nums less than median
        self._gtm: List[tuple[int, int]] = [] # min heap with nums greater than median

    def addNum(self, num: int) -> None:
        if len(self) == 0 or num > self.findMedian():
            heapq.heappush(self._gtm, (num, num))
        else:
            # heappush maintains min heap, so in order to make _ltm a max queue
            # add -item as priority
            heapq.heappush(self._ltm, (-num, num))

    def findMedian(self) -> float:
        self._balance()
        if len(self._ltm) > len(self._gtm):
            return float(self._ltm[0][1])
        if len(self._ltm) < len(self._gtm):
            return float(self._gtm[0][1])
        return (self._ltm[0][1] + self._gtm[0][1]) / 2

    def _balance(self):
        while len(self._gtm) > len(self._ltm) + 1:
            _, item = heapq.heappop(self._gtm)
            heapq.heappush(self._ltm, (-item, item))
        while len(self._ltm) > len(self._gtm) + 1:
            _, item = heapq.heappop(self._ltm)
            heapq.heappush(self._gtm, (item, item))

    def __len__(self):
        return len(self._ltm) + len(self._gtm)
