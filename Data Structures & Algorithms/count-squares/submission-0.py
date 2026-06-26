class CountSquares:

    def __init__(self):
        self.points = {} # hashmap, index is coord, value is number of points

    def add(self, point: List[int]) -> None:
        coord = (point[0], point[1])
        self.points[coord] = self.points.get(coord, 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for px, py in self.points:
            if x == px and y != py:
                delta = py - y

                if (x + delta, y) in self.points and (x + delta, y + delta) in self.points:
                    res += self.points[(px, py)] * self.points[(x + delta, y)] * self.points[(x + delta, y + delta)]
                if (x - delta, y) in self.points and (x - delta, y + delta) in self.points:
                    res += self.points[(px, py)] * self.points[(x - delta, y)] * self.points[(x - delta, y + delta)]

            elif x != px and y == py:
                delta = px - x

                if (x, y + delta) in self.points and (x + delta, y + delta) in self.points:
                    res += self.points[(px, py)] * self.points[(x, y + delta)] * self.points[(x + delta, y + delta)]
                if (x, y - delta) in self.points and (x + delta, y - delta) in self.points:
                    res += self.points[(px, py)] * self.points[(x, y - delta)] * self.points[(x + delta, y - delta)]
        
        return int(res/2)
