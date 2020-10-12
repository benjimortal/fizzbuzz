class Stack:
    def __init__(self):
        self._storage = []

    def push(self, value):
        self._storage.append(value)

    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item

    def __len__(self):
        return len(self._storage)
