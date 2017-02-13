

def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return start



def compose(*fns):
    def _compose_(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

    if not fns:
        return lambda x: x
    elif len(fns) == 1:
        return fns[0]
    else:
        return reduce(_compose_, fns)


class Reduced:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value



class Appender:
    def initial(self):
        return []

    def update(self, result, item):
        result.append(item)
        return result

    def complete(self, result):
        return result


    
def transduce(transducer, reducer, iterable, init=None):
    f = transducer(reducer)
    res = init if init else reducer.initial()

    for x in iterable:
        y = f.update(res, x)
        if isinstance(y, Reduced):
            return y.value
        res = y

    return f.complete(x)
