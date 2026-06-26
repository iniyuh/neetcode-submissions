class MinHeap:
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i // 2 != 0 and self.heap[i] < self.heap[i // 2]:
            self.swap(i, i // 2)
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) <= 1: return -1

        ret = self.heap[1]
        print(self.heap)
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        i = 1

        while i <= len(self.heap) // 2:
            leftLess = self.heap[i] > self.heap[2*i] if len(self.heap) > 2*i else False
            rightLess = self.heap[i] > self.heap[2*i + 1] if len(self.heap) > 2*i + 1 else False

            if not (leftLess or rightLess): break
            elif (not leftLess) and rightLess:
                self.swap(i, 2*i + 1)
                i = 2 * i + 1
            elif (not rightLess) and leftLess:
                self.swap(i, 2*i)
                i = 2 * i
            else:
                if self.heap[2*i] < self.heap[2*i + 1]:
                    self.swap(i, 2*i)
                    i = 2 * i
                else:
                    self.swap(i, 2*i + 1)
                    i = 2 * i + 1
        
        return ret


    def top(self) -> int:
        if len(self.heap) <= 1: return -1
        else: return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        for i in nums:
            self.push(i)
        