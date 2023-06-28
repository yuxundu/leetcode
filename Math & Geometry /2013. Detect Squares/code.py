class DetectSquares:

    def __init__(self):
        self.ptCount = defaultdict(int)
        self.pts = []

        

    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        qx,qy = point
        res = 0
        for px,py in self.pts:
            if abs(qx-px) != abs(qy-py) or qx == px or qy == py:
                continue
            if (qx,py) in self.ptCount and (px,qy) in self.ptCount:
                res += self.ptCount[(qx,py)]*self.ptCount[(px,qy)]
        return res

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)