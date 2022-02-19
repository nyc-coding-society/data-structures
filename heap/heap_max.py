
class HeapMax:
    def __init__(self):
        self.heap = []

    def left(self, n):
        return n * 2 + 1

    def right(self, n):
        return n * 2 + 2

    def parent(self, n):
        return (n - 1) // 2

    def insert(self, n):
        self.heap.append(n)
        self.heapify_up()

    def heapify_up(self):
        pos = len(self.heap) - 1
        while pos != 0:
            parent_pos = self.parent(pos)
            if self.heap[pos] > self.heap[parent_pos]:
                self.heap[pos], self.heap[parent_pos] = self.heap[parent_pos], self.heap[pos]
                pos = parent_pos
            else:
                break

    def get_max(self):
        pass

    def heapify_down(self):
        pass

    def display(self):
        for v in self.heap:
            print(v, end=" ")
        print()


if __name__ == '__main__':
    heap = HeapMax()
    heap.insert(89)
    heap.insert(4)
    heap.insert(56)
    heap.insert(100)
    heap.insert(17)
    heap.insert(39)
    heap.insert(110)

    heap.display()
