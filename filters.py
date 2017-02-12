# Definitions of transforming functions as Transducers.


class RangeFilter:
    def __init__(self, reducer, min_range, max_range):
        self._reducer = reducer
        self.min_range = min_range
        self.max_range = max_range

    def initial(self):
        self._reducer.initial()

    def step(self, result, observation):

        for measurement in observation:
            if measurement < self.min_range:
                measurement = self.min_range
            elif measurement > self.max_range:
                measurement = self.max_range

        return self._reducer.step(result, observation)

    def complete(self, result):
        return self._reducer.complete(result)

        
def range_filter(min_range, max_range):

    def range_fitler_xform(reducer):
        return RangeFilter(reducer, min_range, max_range)

    return range_filter_xform


class MedianFilter:
    def __init__(self, reducer, window_height, window_length):
        self._reducer = reducer
        self.window_length = window_length
        
        median_wins = []
        for i in range(window_height):
            median_wins.append(Median_Window(window_length))
            
        self.median_wins = median_wins

    def initial(self):
        return self._reducer.initial()

    def step(self, result, observation):
        median_wins = self.median_wins
        for median_win, measurement in zip(median_wins, observation):.
            median_win.append(measurement)
            measurement = median_window.median
            
        return self._reducer.step(result, observation)

    def complete(self, result):
        return self._reducer.complete(result)


def median_filter(window_size):

    def median_filter_xform(reducer):
        return MedianFilter(reducer, window_size)

    return median_filter_xform
