class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
         self.storage.append(value)
         self._bubble_up(self.get_size()-1)

    def delete(self):
        if self.get_size() < 1:
            return
        elif self.get_size() == 1:
            return self.storage.pop()
        else:
            self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
            max_val = self.storage.pop()
            self._sift_down(0)
            return max_val

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = (index-1)//2
        current = index
        while current > 0 and self.storage[parent] < self.storage[current]:
            self.storage[current], self.storage[parent] = self.storage[parent], self.storage[current]
            current = parent
            parent = (parent-1)//2


    def _sift_down(self, index):
        biggest = index
        leftchild = 2*biggest+1
        rightchild = 2*biggest+2
        if leftchild < self.get_size() and self.storage[biggest] < self.storage[leftchild]:
            biggest = leftchild
        if rightchild < self.get_size() and self.storage[biggest] < self.storage[rightchild]:
            biggest = rightchild
        if biggest != index:
            self.storage[index], self.storage[biggest] = self.storage[biggest], self.storage[index]
            self._sift_down(biggest)
