class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.count == self.capacity: self.resize()
        self.arr[self.count] = n
        self.count += 1

    def popback(self) -> int:
        self.count -= 1
        return self.arr[self.count]

    def resize(self) -> None:
        self.arr = self.arr + ([0] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.count
    
    def getCapacity(self) -> int:
        return self.capacity