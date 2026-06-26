class CountSquares:

    def __init__(self):
        self.columns = defaultdict(dict)
        self.rows = defaultdict(dict)

        

    def add(self, point: List[int]) -> None:
        x, y = point

        self.columns[x][y] = self.columns[x].get(y, 0) + 1
        self.rows[y][x] = self.rows[y].get(x, 0) + 1
        

    def count(self, point: List[int]) -> int:
        x, y = point

        if x not in self.columns or y not in self.rows: return 0

        mult1 = self.rows[y].get(x, 1)

        count = 0

        for x2, mult2 in self.rows[y].items():
            if x2 == x: continue

            deltaX = x - x2

            if y + deltaX in self.columns[x] and y + deltaX in self.columns[x2]:
                count += mult1 * mult2 * self.columns[x][y + deltaX] * self.columns[x2][y + deltaX]

            if y - deltaX in self.columns[x] and y - deltaX in self.columns[x2]:
                count += mult1 * mult2 * self.columns[x][y - deltaX] * self.columns[x2][y - deltaX]

        return count