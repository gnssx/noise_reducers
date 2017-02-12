from data_structures import MedianWindow


# Definitions of transforming functions as Transducers.
# For rational see:

class RangeFilter:
    def __init__(self, reducer, min_range, max_range):
        self._reducer = reducer
        self.min_range = min_range
        self.max_range = max_range

    def initial(self):
        self._reducer.initial()

    def update(self, result, observation):

        transform = []
        for measurement in observation:
            if measurement < self.min_range:
                measurement = self.min_range
            elif measurement > self.max_range:
                measurement = self.max_range
            transform.append(measurement)

        return self._reducer.update(result, transform)

    def complete(self, result):
        return self._reducer.complete(result)

        
def range_filter(min_range, max_range):

    def range_filter_xform(reducer):
        return RangeFilter(reducer, min_range, max_range)

    return range_filter_xform




class MedianFilter:
    def __init__(self, reducer, window_length):
        self._reducer = reducer
        self.window_length = window_length
        self.median_wins = self._init_window(window_length)

    def _init_window(self, size):
        median_wins = []
        for i in range(size):
            median_wins.append(MedianWindow(size))
        return median_wins

    def initial(self):
        return self._reducer.initial()

    def update(self, result, observation):
        median_wins = self.median_wins
        
        transform = []
        for median_win, measurement in zip(median_wins, observation):
            median_win.append(measurement)
            transform.append(median_win.median)

        return self._reducer.update(result, transform)

    def complete(self, result):
        self.median_wins = self._init_window(self.window_length)
        return self._reducer.complete(result)



def median_filter(window_size):

    def median_filter_xform(reducer):
        return MedianFilter(reducer, window_size)

    return median_filter_xform


    
