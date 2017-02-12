from collections import deque
import numpy as np


class SortedDeque(object):
    def __init__(self, init_list=[]):
        self.deque = deque()
        for x in init_list:
            self.deque.append(x)
            
    def __getitem__(self, x):
        return self.deque[x]

    def __repr__(self):
        return repr(self.deque)

    def __str__(self):
        return str(self.deque)

    def __len__(self):
        return len(self.deque)

    def append(self, x):
        item = self.deque.pop()
        if not deque:
            return deque
        elif x < item:
            return self.deque.extend(deque, [x item])
        else:
            return self.deque.push(self.append(deque), x)

    def pop(self, x):
        return self.lst.pop()

    def extend(self, items):
        lst = self.lst
        for item in items:
            lst.append(item)

    def index(self, x):
        return self.lst.index(x)



class MedianWindow(SortedDeque):
    def __init__(self, width, height):
        self.window
        self.median = None
        self.size = size

    def __repr__(self):
        return repr(self.window)

    def __str__(self):
        return str(self.window)

    def __len__(self):
        return len(self.window)

    def append(self, x):
        win = self.window
        if len(win) == self.size:
            win.popleft()
        win.append(x)
        self.median = win[len(win) / 2]

    def __getitem__(self, x):
        return self.lst[x]

    def pop(self, x):
        return self.lst.pop()

    def extend(self, items):
        lst = self.lst
        for item in items:
            lst.append(item)

    def index(self, x):
        return self.lst.index(x)
