from bisect import bisect_right
from collections import deque

def binary_search(indexable, item):
    low = 0
    hi = len(indexable) - 1
    while True:
        if (low > hi):
            raise ValueError('{0} is not in collection'.format(item))
        else:
            mid = (low + hi) / 2
            if indexable[mid] == item:
                return mid
            elif indexable[mid] < item:
                low = mid+1
            else:
                hi = mid-1


class SortedList(object):
    def __init__(self, init_list=[]):
        lst = []
        for x in init_list:
            lst.append(x)
        self.lst = lst
            
    def __getitem__(self, x):
        return self.lst[x]

    def __repr__(self):
        return repr(self.lst)

    def __delitem__(self, i):
        del self.lst[i]

    def __del__(self):
        del self.lst

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        return iter(self.lst)

    def append(self, x):
        i = bisect_right(self.lst, x)
        self.lst.insert(i, x)

    def pop(self, x):
        return self.lst.pop()

    def extend(self, items):
        lst = self.lst
        for item in items:
            lst.append(item)

    def index(self, x):
        return binary_search(self.lst, x)



class MedianWindow(object):
    def __init__(self, max_size=10, init_list=[]):
        self.window = SortedList(init_list)
        self.deque = deque()
        self._median = None
        
        if max_size < 1:
            raise ValueError('size of window must be at least 1.')

        self.max_size = max_size

    def __repr__(self):
        return repr(self.window)

    def __str__(self):
        return str(self.window)

    def __len__(self):
        return len(self.window)

    def __iter__(self):
        return iter(self.window)

    def append(self, x):
        win = self.window
        queue = self.deque
        size = self.max_size

        if len(win) > size:
            del win[win.index(queue.popleft())]

        win.append(x)
        queue.append(x)
        if len(win) % 2 == 1:
            self._median = win[len(win) / 2]
        else:
            m0 = win[len(win) / 2]
            m1 = win[(len(win) / 2) - 1]
            self._median = (m0 + m1) / 2


    def __getitem__(self, x):
        return self.lst[x]

    
    def extend(self, items):
        for item in items:
            self.append(item)

    def index(self, x):
        return self.lst.index(x)

    @property
    def median(self):
        return self._median
