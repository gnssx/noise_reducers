from bisect import bisect_right


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
        return self.lst.index(x)



class MedianWindow(object):
    def __init__(self, max_size, init_list=[]):
        self.window = SortedList(init_list)
        self._median = None
        self.max_size = max_size

    def __repr__(self):
        return repr(self.window)

    def __str__(self):
        return str(self.window)

    def __len__(self):
        return len(self.window)

    def __delitem__(self, i):
        del self.window[i]

    def __iter__(self):
        return iter(self.window)

    def append(self, x):
        win = self.window
        size = self.max_size

        if len(win) == size:
            del win[0]

        win.append(x)
        self._median = win[len(win) / 2]
            
        

    def __getitem__(self, x):
        return self.lst[x]

    def pop(self, x):
        self.lst.pop()
        self._median = win[len(win) / 2] if win else None
        return self.lst

    def extend(self, items):
        win = self.window
        for item in items:
            win.append(item)

    def index(self, x):
        return self.lst.index(x)

    @property
    def median(self):
        return self._median
