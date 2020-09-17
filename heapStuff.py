from heapq import heapify, heappop, heappush, heapreplace


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) / 2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2

    # insert key into heap
    def insert(self, k):
        heappush(self.heap, k)

    # extracts min element
    def extract_min(self):
        return heappop(self.heap)

    # get min without extracting
    def get_min(self):
        return self.heap[0]

    # delete key
    def remove(self, x):
        pass

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])

    # removes element at index i
    def delete_key(self, i):
        self.decrease_key(i, float('-inf'))
        self.extract_min()


my_heap = MinHeap()
for x in [9, 5, 8, 13, 4, 7, 8, 9, 0, 4, 7, 6, 5, 0.5]:
    my_heap.insert(x)
print(my_heap.heap)
my_heap.insert(-4)
print(my_heap.heap)
print(my_heap.extract_min())
print(my_heap.heap)
my_array = [23, 4, 15, 6, 9, 16, 53, 7, 75]
heapify(my_array)
print(my_array)