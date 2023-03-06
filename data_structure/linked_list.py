class LinkedList:
    def __init__(self, arr):
        self._arr = arr
        if not self._arr:
            self.head = None
        else:
            self.head = self._arr[0]
            self.head_index = 0

    def next(self):
        self.head_index += 1
        if self.head_index > len(self._arr) - 1:
            self.head = None
            print(f'LinkedList is over, head = {self.head}')
        else:
            prev_head = self.head
            self.head = self._arr[self.head_index]
            print(f'head: {prev_head} -> {self.head}')

    def __repr__(self):
        return f'head = {self.head}'
